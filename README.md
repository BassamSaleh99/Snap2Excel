# Snap2Excel

## Table and Column Detection from Document Images

This project focuses on detecting tables and their column structures in scanned or digital document images using a dual-output deep learning model. The detected tables are then extracted and converted into editable Excel files.

### 🧠 Model Architecture

The model is based on a modified **VGG19 backbone** with two output heads:
- `table_mask`: Predicts the overall table regions.
- `col_mask`: Predicts column segmentation within the detected tables.

The architecture is trained using `sparse_categorical_crossentropy` for both outputs.

### 📁 Dataset

We use the **Marmot Extended Dataset** which contains:
- Document images with varying layouts.
- Annotations for table boundaries and column structures (converted into segmentation masks).

### 🛠️ Features

- Table and column segmentation from images.
- Conversion of detected tables to structured Excel files.
- Heuristic-based post-processing to refine table boundaries.
- Custom training with image size 512×512 and mask generation.

### 🔧 Dependencies

- Python 3.8+
- TensorFlow / Keras
- OpenCV
- NumPy
- Matplotlib
- Pandas
- `openpyxl` (for Excel writing)