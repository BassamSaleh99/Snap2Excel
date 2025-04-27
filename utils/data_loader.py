{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "104a8ecd-e157-4f78-90d8-a83c50d82e00",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "import json\n",
    "import os\n",
    "\n",
    "def load_image(image_path):\n",
    "    image = cv2.imread(image_path)\n",
    "    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)\n",
    "\n",
    "def load_annotation(annotation_path):\n",
    "    with open(annotation_path, 'r', encoding='utf-8') as f:\n",
    "        annotation = f.read()\n",
    "    return annotation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a750aa6d-9d81-47e1-a5b1-1e9e34a6fd2e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.14 (tensorflow)",
   "language": "python",
   "name": "tensorflow"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
