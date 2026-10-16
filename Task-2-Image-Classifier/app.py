
from pathlib import Path

import streamlit as st
import torch
from torch import nn
from torchvision import models, transforms
from PIL import Image

BASE_DIR = Path(__file__).parent
MODEL_PATH = BASE_DIR / "cat_dog_model.pth"

st.set_page_config(
    page_title="AI Cat vs Dog Classifier",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 AI Cat vs Dog Classifier")
st.write(
    "Upload a cat or dog image. Our transfer-learning model "
    "will predict which animal appears in the image."
)

@st.cache_resource
def load_model():
    checkpoint = torch.load(
        MODEL_PATH,
        map_location="cpu",
        weights_only=True
    )

    classes = checkpoint["classes"]
    image_size = checkpoint["image_size"]

    model = models.resnet18(weights=None)
    model.fc = nn.Linear(model.fc.in_features, len(classes))
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()

    return model, classes, image_size

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

uploaded_file = st.file_uploader(
    "Choose a cat or dog photo",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded image", use_container_width=True)

        with st.spinner("Analyzing image..."):
            model, classes, image_size = load_model()
            input_tensor = transform(image).unsqueeze(0)

            with torch.no_grad():
                outputs = model(input_tensor)
                probabilities = torch.softmax(outputs, dim=1)[0]

            predicted_index = int(probabilities.argmax())
            predicted_class = classes[predicted_index]
            confidence = float(probabilities[predicted_index]) * 100

        st.success(f"Prediction: {predicted_class.title()} 🐾")
        st.metric("Model confidence", f"{confidence:.2f}%")

        st.subheader("Class probabilities")
        for index, class_name in enumerate(classes):
            score = float(probabilities[index])
            st.write(f"{class_name.title()}: {score * 100:.2f}%")
            st.progress(score)

        st.caption(
            "This model is trained to distinguish cats from dogs. "
            "Predictions may be unreliable for other types of images."
        )

    except Exception as error:
        st.error(f"Could not analyze this image: {error}")
else:
    st.info("Upload an image above to get a prediction.")
