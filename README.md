# DATA-COMPRESSION
# 🧬 CGR-Based DNA Visualization

This project implements **Chaos Game Representation (CGR)** to convert DNA sequences into unique, interpretable visual patterns. CGR maps the 1D nucleotide sequence into a 2D image, providing insights into genomic structure, sequence complexity, and possible mutations.

---

## 🔍 Overview

CGR is a powerful technique to visualize long DNA sequences in a 2D coordinate system. Each base (A, T, C, G) is mapped to a corner of a square, and subsequent points are plotted based on recursive midpoint calculations.

This project supports:
- Reading DNA sequences (from string or FASTA)
- Generating high-resolution CGR plots
- Saving outputs for presentation or research purposes

---

## 🧪 Example Output

![image](https://github.com/user-attachments/assets/5793e97a-fc1c-47e7-a51c-95d6f66250b9)


---

## 🧠 How It Works

1. Start from the center of a square.
2. Move halfway toward the corresponding corner for each nucleotide:
   - A → Top-left
   - T → Top-right
   - C → Bottom-left
   - G → Bottom-right
3. Plot the point.
4. Repeat for the entire sequence.

---

## How to use this
do ## pip install gradio matplotlib numpy in your terminal
then run the python file directly after installing that libraries
