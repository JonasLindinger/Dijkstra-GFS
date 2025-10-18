<!-- 🤖 AI-GENERATED README -->
# 🧭 Dijkstra Algorithm Visualization – GFS Project

A **visual deep dive** into one of computer science’s most famous algorithms — **Dijkstra’s Shortest Path Algorithm** — brought to life with **Manim CE (Community Edition)**.  
This project demonstrates and compares **Lazy** and **Eager** implementations of Dijkstra’s algorithm through smooth mathematical animations.

---

## 🎥 Overview

This project was created for my **GFS (German "Gleichwertige Feststellung von Schülerleistungen")** presentation.  
It’s not just theory — it’s a **fully animated explanation** powered by Python and Manim CE.

### ✨ Features
- 🔁 **Two algorithm versions:** Lazy Dijkstra & Eager Dijkstra  
- 🎬 **Smooth visualizations** of each algorithm step  
- 🧮 **Graph-based examples** with changing weights and paths  
- 🧠 **Educational focus:** each frame helps understand how the algorithm really *thinks*  

---

## 🧩 Algorithms Implemented

| Algorithm | Description |
|------------|--------------|
| **Lazy Dijkstra** | A simpler implementation where outdated entries can stay in the priority queue. Easier to code, but slightly less efficient. |
| **Eager Dijkstra** | Optimized version that updates node distances directly, avoiding outdated queue entries. Faster and cleaner. |

---

## 🛠️ Tech Stack

- 🐍 **Python 3**
- 🎨 **[Manim CE](https://docs.manim.community/)** – mathematical animation engine
- 💡 **Custom Visualization Utilities** (highlighting paths, weights, and queue updates)

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/<your-username>/GFS-Dijkstra-Visualization.git
cd GFS-Dijkstra-Visualization

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # on Linux/macOS
venv\Scripts\activate     # on Windows

# Install dependencies
pip install -r requirements.txt

# Render a specific scene
manim -pql main.py DijkstraLazyScene
# or
manim -pql main.py DijkstraEagerScene

```
💡 Tip: Use -pqh for high-quality output!

🧠 Concept Behind the Visualization

The animation visually represents:

Priority queue operations

Distance updates to each node

The difference between lazy and eager updates

How the shortest path "emerges" step by step

Each node and edge dynamically changes color to reflect real-time algorithmic updates — helping you see how Dijkstra "thinks" in motion.


🧾 License

This project is released under the MIT License.
Feel free to learn from it, remix it, or use it for your own GFS!

👤 Author

Jonas Lindinger
🎓 GFS Project 2025
💬 Exploring algorithms visually with Python and Manim

⭐ If you found this project helpful or inspiring, consider leaving a star on GitHub!

---

Would you like me to make it include a **“comparison table with time complexity and memory usage”** for the two Dijkstra variants too? That could make it look even more professional for a GFS presentation.

