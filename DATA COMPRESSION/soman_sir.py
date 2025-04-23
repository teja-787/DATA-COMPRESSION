import gradio as gr
import matplotlib.pyplot as plt

# Define mapping for CGR corners
corner_map = {'A': (0, 0), 'C': (0, 1), 'G': (1, 1), 'T': (1, 0)}

def plot_cgr(sequence):
    sequence = sequence.upper()
    # Filter invalid characters
    sequence = ''.join([base for base in sequence if base in corner_map])
    
    x, y = 0.5, 0.5  # Start from center
    x_vals, y_vals = [x], [y]

    for base in sequence:
        corner_x, corner_y = corner_map[base]
        x = (x + corner_x) / 2
        y = (y + corner_y) / 2
        x_vals.append(x)
        y_vals.append(y)

    plt.figure(figsize=(5, 5))
    plt.plot(x_vals, y_vals, 'k.', markersize=0.5)
    plt.title("Chaos Game Representation (CGR)")
    plt.axis('off')

    # Save and return the plot
    plot_path = "cgr_output.png"
    plt.savefig(plot_path, bbox_inches='tight', dpi=300)
    plt.close()
    return plot_path

# Gradio interface
demo = gr.Interface(fn=plot_cgr,
                    inputs=gr.Textbox(lines=5, placeholder="Enter DNA sequence (e.g., ATCGTACG)..."),
                    outputs="image",
                    title="CGR Bio-sequence Visualizer",
                    description="Enter a DNA sequence (using A, T, C, G). The CGR plot shows its unique fractal pattern.")

demo.launch()
