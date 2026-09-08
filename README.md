<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f6feb,100:0d1117&height=120&section=header" width="100%" alt=""/>

# Tomáš Řádek

*High school student in the Czech Republic. Represented Czechia at the International Olympiad in AI (IOAI) 2026 in Astana, after placing 1st nationally in the Czech AI Olympiad selection.*

<img src="https://readme-typing-svg.demolab.com/?font=JetBrains+Mono&size=15&pause=1200&color=4493F8&center=true&vCenter=true&width=560&lines=Building+AI+systems+and+games;Learning+by+building%2C+not+just+reading" alt="Typing SVG" />

</div>

<br>

## Projects

### Prizma
A local chat app that routes every prompt to the best free LLM available, using only API keys you configure yourself — no proxy account, no shared keys, everything stored in the OS credential store. A planner model reads the request first and briefs whichever model answers it; if the planner fails or the request is trivial, a heuristic classifier takes over, and the router fails over to another provider automatically when one hits a rate limit.

<sub>Python · FastAPI · LiteLLM · React · SQLite</sub>

### Iron Dust
A turn-based economy-strategy game set in 1872 on the American frontier, built in Godot with an isometric 2.5D view. Resource production, a branching tech tree, territory and settlements, trade, and combat against an AI faction that actively expands and attacks — rule-based for now, with a reinforcement-learning version planned once the scripted opponent is properly balanced.

<sub>Godot 4 · GDScript</sub>

### Wi-Fi Radar
A local dashboard that tracks devices on my home network and estimates which room they're in. The router doesn't expose RSSI, so it calibrates against link speed and response latency instead, and reports a confidence level rather than a distance it can't actually back up.

<sub>Python · FastAPI · SQLite · React · TypeScript · Chrome extension</sub>

### OP sys
A control layer for switching work modes on Windows — restores project context and flags which processes don't belong in the current mode, but never closes anything without confirmation. Modes are just TOML profiles with inheritance, not code, so adding one doesn't touch the app.

<sub>TypeScript · Rust · Tauri</sub>

<br>

<sub>Most of this is still moving — commit history is more current than this page.</sub>
