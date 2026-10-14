
from flask import Flask, render_template_string, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NEXORA | DevOps Deployment Platform</title>
<style>
:root {
    --bg: #080d19;
    --panel: #101a2d;
    --panel2: #14213a;
    --border: #243550;
    --text: #edf4ff;
    --muted: #91a2bd;
    --blue: #48a9ff;
    --cyan: #4de0d1;
    --green: #35d69a;
}
* { margin:0; padding:0; box-sizing:border-box; }
html { scroll-behavior:smooth; }
body {
    font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background:var(--bg);
    color:var(--text);
    line-height:1.6;
}
a { text-decoration:none; color:inherit; }
.container { width:min(1160px,90%); margin:auto; }

header {
    position:relative;
    overflow:hidden;
    background:
      radial-gradient(ellipse at 80% 25%,#233c75 0%,transparent 45%),
      radial-gradient(ellipse at 10% 90%,#103c50 0%,transparent 40%),
      #080d19;
    border-bottom:1px solid var(--border);
}
nav {
    height:85px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    border-bottom:1px solid #ffffff12;
}
.logo { font-size:25px; font-weight:850; letter-spacing:1px; }
.logo span { color:var(--blue); }
.navlinks { display:flex; gap:30px; color:#b5c3d9; font-size:14px; }
.navlinks a:hover { color:var(--cyan); }
.nav-status {
    padding:8px 14px;
    border:1px solid #35d69a55;
    background:#35d69a12;
    color:var(--green);
    border-radius:30px;
    font-size:12px;
}
.hero {
    min-height:520px;
    display:grid;
    grid-template-columns:1.1fr .9fr;
    gap:55px;
    align-items:center;
    padding:75px 0 90px;
}
.eyebrow {
    display:inline-flex;
    align-items:center;
    gap:9px;
    border:1px solid #48a9ff44;
    color:#91caff;
    background:#48a9ff12;
    border-radius:30px;
    padding:8px 15px;
    font-size:12px;
    font-weight:700;
}
.dot {
    width:7px; height:7px; border-radius:50%;
    background:var(--green);
    box-shadow:0 0 12px var(--green);
}
h1 {
    font-size:clamp(43px,5.5vw,70px);
    line-height:1.07;
    letter-spacing:-2.5px;
    margin:25px 0;
}
.gradient {
    background:linear-gradient(100deg,#52bdff,#7c83ff,#5be3d0);
    -webkit-background-clip:text;
    background-clip:text;
    color:transparent;
}
.hero p { max-width:560px; color:#aab9d0; font-size:16px; line-height:1.9; }
.actions { display:flex; gap:14px; flex-wrap:wrap; margin-top:32px; }
.btn {
    padding:13px 21px;
    border-radius:9px;
    font-size:14px;
    font-weight:750;
    transition:.2s;
}
.btn-primary {
    color:#07101e;
    background:linear-gradient(100deg,#58c3ff,#55dfce);
}
.btn-secondary { border:1px solid #526582; color:white; }
.btn:hover { transform:translateY(-3px); }

.pipeline-card {
    background:linear-gradient(145deg,#152641,#0d172a);
    border:1px solid #344968;
    padding:26px;
    border-radius:20px;
    box-shadow:0 25px 80px #0007;
}
.panel-heading {
    display:flex; justify-content:space-between;
    align-items:center; margin-bottom:23px;
}
.panel-heading small { color:var(--muted); }
.live-label { color:var(--green); font-size:11px; }
.pipeline-list { display:flex; flex-direction:column; gap:11px; }
.pipeline-step {
    display:flex; align-items:center; gap:15px;
    background:#ffffff08;
    border:1px solid #ffffff12;
    border-radius:12px;
    padding:14px;
}
.step-icon {
    width:43px; height:43px;
    display:grid; place-items:center;
    border-radius:11px;
    background:#48a9ff18;
    font-size:21px;
}
.step-info { flex:1; }
.step-info b { display:block; font-size:14px; }
.step-info small { color:var(--muted); font-size:11px; }
.check { color:var(--green); font-size:19px; }
.connector { margin-left:34px; height:10px; border-left:1px dashed #57708e; }

section { padding:75px 0; }
.section-head { margin-bottom:32px; }
.section-head small {
    color:var(--cyan); text-transform:uppercase;
    font-weight:800; letter-spacing:2px; font-size:11px;
}
.section-head h2 { font-size:32px; margin-top:9px; letter-spacing:-1px; }
.section-head p { color:var(--muted); margin-top:8px; }

.stats {
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:16px;
}
.stat, .card, .tech {
    background:var(--panel);
    border:1px solid var(--border);
    border-radius:15px;
}
.stat { padding:23px; }
.stat small { color:var(--muted); font-size:12px; }
.stat h3 { font-size:28px; margin:9px 0 2px; }
.stat span { color:var(--green); font-size:11px; }

.content-grid {
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:18px;
}
.card { padding:25px; transition:.25s; }
.card:hover, .tech:hover {
    transform:translateY(-5px);
    border-color:#48a9ff77;
}
.card-icon { font-size:27px; margin-bottom:18px; }
.card h3 { font-size:18px; margin-bottom:11px; }
.card p { color:var(--muted); font-size:13px; line-height:1.8; }
.card ul { list-style:none; margin-top:15px; }
.card li { color:#bac8dc; font-size:13px; margin:10px 0; }
.card li::before { content:"✓  "; color:var(--green); }

.tech-grid {
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:15px;
}
.tech { text-align:center; padding:23px 10px; }
.tech div { font-size:29px; margin-bottom:10px; }
.tech b { font-size:13px; }

.status-card {
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:20px;
    flex-wrap:wrap;
    padding:26px;
    background:linear-gradient(100deg,#102a2b,#11243a);
    border:1px solid #35d69a55;
    border-radius:16px;
}
.status-card h3 { font-size:19px; }
.status-card p { color:#9bb9b7; font-size:13px; margin-top:5px; }
.status-pill {
    padding:10px 16px;
    border-radius:30px;
    background:#35d69a19;
    border:1px solid #35d69a55;
    color:var(--green);
    font-size:12px;
    font-weight:800;
}
footer {
    border-top:1px solid var(--border);
    padding:28px 0;
    color:var(--muted);
    font-size:12px;
}
.footer-inner {
    display:flex; justify-content:space-between;
    flex-wrap:wrap; gap:12px;
}
footer b { color:white; }

@media(max-width:850px) {
    .hero { grid-template-columns:1fr; padding:60px 0; }
    .stats { grid-template-columns:repeat(2,1fr); }
    .content-grid { grid-template-columns:1fr 1fr; }
    .tech-grid { grid-template-columns:repeat(3,1fr); }
}
@media(max-width:550px) {
    nav { height:auto; padding:20px 0; align-items:flex-start; }
    .navlinks { display:none; }
    .hero { gap:35px; }
    h1 { letter-spacing:-1.5px; }
    .content-grid { grid-template-columns:1fr; }
    .tech-grid { grid-template-columns:repeat(2,1fr); }
    section { padding:50px 0; }
    .section-head h2 { font-size:26px; }
}
</style>
</head>
<body>

<header id="home">
<div class="container">
<nav>
    <a href="#home" class="logo">⬡ NEX<span>ORA</span></a>
    <div class="navlinks">
        <a href="#overview">Overview</a>
        <a href="#pipeline">Pipeline</a>
        <a href="#technology">Technology</a>
        <a href="#about">About</a>
    </div>
    <div class="nav-status">● SYSTEM ONLINE</div>
</nav>

<div class="hero">
    <div>
        <span class="eyebrow"><span class="dot"></span> AUTOMATED CI/CD DEPLOYMENT</span>
        <h1>Build. Ship.<br><span class="gradient">Deploy.</span></h1>
        <p>
            Experience a modern Continuous Integration and Continuous
            Deployment workflow. NEXORA demonstrates how application
            code moves from development to a cloud-ready Docker deployment
            through Jenkins and AWS infrastructure.
        </p>
        <div class="actions">
            <a href="#pipeline" class="btn btn-primary">Explore Pipeline ↗</a>
            <a href="#technology" class="btn btn-secondary">Explore Technology</a>
        </div>
    </div>

    <div class="pipeline-card" id="pipeline">
        <div class="panel-heading">
            <div>
                <b>Deployment Workflow</b><br>
                <small>Automated delivery process</small>
            </div>
            <span class="live-label">● WORKFLOW</span>
        </div>

        <div class="pipeline-list">
            <div class="pipeline-step">
                <div class="step-icon">🐙</div>
                <div class="step-info"><b>GitHub</b><small>Source code management</small></div>
                <span class="check">✓</span>
            </div>
            <div class="connector"></div>
            <div class="pipeline-step">
                <div class="step-icon">⚙️</div>
                <div class="step-info"><b>Jenkins</b><small>Continuous integration</small></div>
                <span class="check">✓</span>
            </div>
            <div class="connector"></div>
            <div class="pipeline-step">
                <div class="step-icon">🐳</div>
                <div class="step-info"><b>Docker</b><small>Container image build</small></div>
                <span class="check">✓</span>
            </div>
            <div class="connector"></div>
            <div class="pipeline-step">
                <div class="step-icon">☁️</div>
                <div class="step-info"><b>AWS Cloud</b><small>Cloud infrastructure</small></div>
                <span class="check">✓</span>
            </div>
        </div>
    </div>
</div>
</div>
</header>

<main>
<section id="overview">
<div class="container">
    <div class="section-head">
        <small>Platform overview</small>
        <h2>Deployment at a glance</h2>
        <p>A showcase of the NEXORA DevOps learning environment.</p>
    </div>
    <div class="stats">
        <div class="stat"><small>Application</small><h3>Flask</h3><span>● Python backend</span></div>
        <div class="stat"><small>Containerization</small><h3>Docker</h3><span>● Container ready</span></div>
        <div class="stat"><small>Automation</small><h3>Jenkins</h3><span>● CI/CD workflow</span></div>
        <div class="stat"><small>Infrastructure</small><h3>AWS</h3><span>● EC2 environment</span></div>
    </div>
</div>
</section>

<section id="about">
<div class="container">
    <div class="section-head">
        <small>What we deliver</small>
        <h2>Designed for modern deployment</h2>
        <p>A simple demonstration of core DevOps practices.</p>
    </div>
    <div class="content-grid">
        <div class="card">
            <div class="card-icon">🚀</div>
            <h3>Continuous Integration</h3>
            <p>Source code changes can be integrated and validated through an automated Jenkins build process.</p>
            <ul><li>Version control</li><li>Automated builds</li><li>Build feedback</li></ul>
        </div>
        <div class="card">
            <div class="card-icon">📦</div>
            <h3>Containerization</h3>
            <p>Docker packages the Flask application and its dependencies into a portable container image.</p>
            <ul><li>Consistent environment</li><li>Dependency management</li><li>Portable deployment</li></ul>
        </div>
        <div class="card">
            <div class="card-icon">☁️</div>
            <h3>Cloud Infrastructure</h3>
            <p>AWS EC2 provides the compute environment for hosting and running the application.</p>
            <ul><li>Cloud hosting</li><li>Network access</li><li>Scalable architecture</li></ul>
        </div>
    </div>
</div>
</section>

<section id="technology">
<div class="container">
    <div class="section-head">
        <small>Technology stack</small>
        <h2>Powered by these technologies</h2>
        <p>Tools used to build and deploy this demonstration.</p>
    </div>
    <div class="tech-grid">
        <div class="tech"><div>🐍</div><b>Python</b></div>
        <div class="tech"><div>🌶️</div><b>Flask</b></div>
        <div class="tech"><div>🐳</div><b>Docker</b></div>
        <div class="tech"><div>⚙️</div><b>Jenkins</b></div>
        <div class="tech"><div>☁️</div><b>AWS EC2</b></div>
    </div>
</div>
</section>

<section>
<div class="container">
    <div class="status-card">
        <div>
            <h3>Application health monitoring</h3>
            <p>Check the Flask health endpoint to verify that the application is responding.</p>
        </div>
        <a href="/health" class="status-pill">VIEW HEALTH STATUS ↗</a>
    </div>
</div>
</section>
</main>

<footer>
<div class="container footer-inner">
    <div><b>⬡ NEXORA</b> &nbsp; | &nbsp; DevOps Deployment Showcase</div>
    <div>Built with Flask, Docker, Jenkins and AWS · © 2026</div>
</div>
</footer>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "NEXORA",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
