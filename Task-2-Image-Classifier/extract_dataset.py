
from pathlib import Path
from zipfile import ZipFile
from PIL import Image
import io

zip_path = Path(r"C:\Users\bharg\Downloads\kagglecatsanddogs_5340.zip")
base = Path(__file__).parent

counts = {"Cat": 0, "Dog": 0}
skipped = 0

with ZipFile(zip_path) as z:
    for name in z.namelist():
        parts = name.replace("\\", "/").split("/")

        if len(parts) != 3 or parts[0] != "PetImages":
            continue

        animal = parts[1]
        if animal not in counts or not name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        try:
            data = z.read(name)

            with Image.open(io.BytesIO(data)) as im:
                im.verify()

            folder = "cats" if animal == "Cat" else "dogs"
            target = base / "dataset" / folder
            target.mkdir(parents=True, exist_ok=True)
            (target / (Path(parts[2]).stem + ".jpg")).write_bytes(data)
            counts[animal] += 1

        except Exception:
            skipped += 1

print("Cat images:", counts["Cat"])
print("Dog images:", counts["Dog"])
print("Skipped invalid images:", skipped)
print("Dataset extraction complete!")
