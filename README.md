# ProjectFireRed – 2D Top-Down Game Engine

## Overview
**ProjectFireRed** is a 2D top-down game engine developed in **pure Java** without using any external game frameworks.  
The project focuses on **core software engineering principles** such as object-oriented design, real-time game loops, state management, collision detection, and modular architecture.

This project was built to gain a deeper understanding of how real-time systems work internally by implementing rendering, input handling, and gameplay logic from scratch.

---

## Tech Stack
- **Language:** Java  
- **Graphics:** Java AWT / Swing  
- **Concepts:** OOP, Game Loop, Collision Detection, State Management  
- **Tools:** Git, IntelliJ IDEA  

---

## Key Features

### 🔁 Game Loop Architecture
- Implemented a continuous **update–render cycle**
- Handles real-time game state updates and rendering
- Clear separation between game logic and drawing logic

### 🗺️ Tile-Based Map System
- Designed a grid-based world using tile maps
- Supports different terrain types
- Scalable structure for adding new maps or levels

### 🚶 Player Movement & Input Handling
- Keyboard-based player movement
- Event-driven input handling
- Frame-independent updates for smooth gameplay

### 🧱 Collision Detection
- Implemented collision logic to prevent invalid movement
- Ensures correct interaction between player and environment
- Uses bounding-based collision checks for efficiency

### 🧩 Object-Oriented Design
- Clean separation of responsibilities across classes
- Modular and maintainable code structure
- Easy to extend with new features or mechanics

### 🎨 Sprite Rendering & Resource Management
- Rendered sprites using Java Graphics APIs
- Managed game assets through structured resource loading

---

## Project Structure
---
ProjectFireRed
│
├── src
│ ├── main
│ │ ├── Main.java
│ │ ├── GamePanel.java
│ │ ├── KeyHandler.java
│ │ ├── Player.java
│ │ └── TileManager.java
│
├── resources
│ ├── player
│ └── tiles
│
└── README.md
---

## What This Project Demonstrates
- Strong **Core Java** fundamentals  
- Real-time system design using a game loop  
- Object-oriented programming and modular architecture  
- Logical problem-solving for movement, collision, and rendering  
- Performance awareness in continuous update systems  

---

## Future Enhancements
- Save and load game state
- Config-driven levels (JSON/YAML)
- NPC movement or basic AI
- Performance optimizations for larger maps

---

## How to Run
1. Clone the repository
- git clone https://github.com/lakshyajoshii/ProjectFireRed.git

2. Open the project in IntelliJ IDEA or Eclipse
3. Run `Main.java`

---

## Author
**Lakshya Joshi**  