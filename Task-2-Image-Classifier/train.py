
from pathlib import Path
import random

import torch
from torch import nn
from torch.utils.data import DataLoader, Subset
from torchvision import datasets, transforms, models

# Reproducible results
random.seed(42)
torch.manual_seed(42)

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "dataset"
MODEL_PATH = BASE_DIR / "cat_dog_model.pth"

BATCH_SIZE = 16
MAX_IMAGES_PER_CLASS = 1000
EPOCHS = 3
IMAGE_SIZE = 224

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Training device:", device)

transform = transforms.Compose([
    transforms.Resize((IMAGE_SIZE, IMAGE_SIZE)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

dataset = datasets.ImageFolder(DATA_DIR, transform=transform)
print("Classes:", dataset.classes)

# Select a manageable, balanced subset from both classes
class_indices = {name: [] for name in dataset.classes}

for index, (_, label) in enumerate(dataset.samples):
    class_name = dataset.classes[label]
    class_indices[class_name].append(index)

selected_indices = []
for class_name, indices in class_indices.items():
    random.shuffle(indices)
    selected_indices.extend(indices[:MAX_IMAGES_PER_CLASS])

random.shuffle(selected_indices)
subset = Subset(dataset, selected_indices)

# Split into training and validation sets
val_size = max(1, int(len(subset) * 0.2))
train_size = len(subset) - val_size
train_data, val_data = torch.utils.data.random_split(
    subset,
    [train_size, val_size],
    generator=torch.Generator().manual_seed(42)
)

train_loader = DataLoader(
    train_data, batch_size=BATCH_SIZE, shuffle=True, num_workers=0
)
val_loader = DataLoader(
    val_data, batch_size=BATCH_SIZE, shuffle=False, num_workers=0
)

# Load pretrained ResNet18
weights = models.ResNet18_Weights.DEFAULT
model = models.resnet18(weights=weights)

# Freeze pretrained feature layers
for param in model.parameters():
    param.requires_grad = False

# Train the final classification layer
model.fc = nn.Linear(model.fc.in_features, len(dataset.classes))
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)

for epoch in range(EPOCHS):
    model.train()
    running_loss = 0.0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)

    train_loss = running_loss / len(train_data)

    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in val_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            predictions = outputs.argmax(dim=1)
            correct += (predictions == labels).sum().item()
            total += labels.size(0)

    accuracy = 100 * correct / total
    print(
        f"Epoch {epoch + 1}/{EPOCHS} | "
        f"Loss: {train_loss:.4f} | "
        f"Validation accuracy: {accuracy:.2f}%"
    )

torch.save({
    "model_state_dict": model.state_dict(),
    "classes": dataset.classes,
    "image_size": IMAGE_SIZE
}, MODEL_PATH)

print(f"Model saved to: {MODEL_PATH}")
