import { research, milestones } from "./lib/research";
import Explorer from "./components/Explorer";
const REPO="https://github.com/dhinchcliffe/PhysicsResearch";
const ATLAS="https://docs.google.com/document/d/1rkQ5z3phVVdCVBP6Obtn3HBA1U6YbQ9L78HwgeqdGAc";
function Arrow({diagonal=false}) { return <span className="arrow" aria-hidden="true">{diagonal?"↗":"→"}</span>; }
function BranchStudy(){
 return <svg className="branch-study" viewBox="0 0 720 360" role="img" aria-labelledby="study-title study-desc">
  <title id="study-title">Four paths, one gravitational interaction</title>
  <desc id="study-desc">Two masses each occupy left or right alternatives, making four joint paths with different interaction phases.</desc>
  <defs><linearGradient id="linewash" x1="0" x2="1"><stop offset="0%" stopColor="#a76c54" stopOpacity=".9"/><stop offset="100%" stopColor="#a76c54" stopOpacity=".13"/></linearGradient><radialGradient id="particle" cx="32%" cy="28%"><stop stopColor="#efcfb6"/><stop offset="100%" stopColor="#a56b51"/></radialGradient></defs>
  <g stroke="#a7aba6" strokeOpacity=".3" strokeWidth="1">
    {[80,160,240,320].map(y=><line key={y} x1="22" y1={y} x2="698" y2={y} strokeDasharray="3 8"/>)}
    {[100,260,460,620].map(x=><line key={x} x1={x} y1="18" x2={x} y2="345" strokeDasharray="3 8"/>)}
  </g>
  <g fill="none" stroke="url(#linewash)" strokeWidth="1.5">
    <path d="M167 110 C320 66 418 76 556 111"/><path d="M167 110 C321 140 408 219 556 258" strokeDasharray="5 7"/><path d="M167 255 C306 233 408 170 556 111" strokeDasharray="5 7"/><path d="M167 255 C316 303 432 300 556 258"/>
  </g>
  <g stroke="#c6c4bc" strokeWidth="1.1" fill="none"><path d="M155 109 H97 V253 H155"/><path d="M568 109 H624 V253 H568"/></g>
  <g fill="url(#particle)" stroke="#8e614e" strokeWidth="1.5">
    {[110,255].map(y=><circle key={"a"+y} cx="167" cy={y} r="14"/>)}
    {[110,255].map(y=><circle key={"b"+y} cx="556" cy={y} r="14"/>)}
  </g>
  <g fill="#686a64" fontFamily="Georgia,serif" fontSize="15"><text x="160" y="62" textAnchor="middle">mass A</text><text x="555" y="62" textAnchor="middle">mass B</text></g>
  <g fill="#777972" fontFamily="ui-monospace,monospace" fontSize="12"><text x="126" y="114" textAnchor="end">L</text><text x="126" y="259" textAnchor="end">R</text><text x="592" y="114">L</text><text x="592" y="259">R</text></g>
  <rect x="289" y="159" width="142" height="48" rx="24" fill="#f4f1e9" stroke="#cdbfb4"/>
  <text x="360" y="180" fill="#493e35" fontFamily="Georgia,serif" fontSize="15" textAnchor="middle">gravity</text>
  <text x="360" y="195" fill="#867d72" fontFamily="ui-monospace,monospace" fontSize="9" textAnchor="middle">FOUR JOINT PATHS</text>
  <text x="25" y="345" fill="#9c9a91" fontFamily="ui-monospace,monospace" fontSize="10">FIG. 01 · SCHEMATIC / NOT TO SCALE</text>
 </svg>;
}
function ProgressRing({completed,total}) {
 const radius=67,circumference=2*Math.PI*radius;
 return <svg viewBox="0 0 180 180" className="progress-ring" role="img" aria-label={completed+" of "+total+" planned research gates completed"}>
 <circle cx="90" cy="90" r={radius} stroke="#deded7" strokeWidth="7" fill="none"/>
 <circle cx="90" cy="90" r={radius} stroke="#9b5b44" strokeWidth="7" fill="none" strokeDasharray={circumference} strokeDashoffset={circumference*(1-completed/total)} strokeLinecap="round" transform="rotate(-90 90 90)"/>
 <text x="90" y="88" textAnchor="middle" fill="#202622" fontSize="34" fontFamily="Georgia,serif">{completed}<tspan fontSize="18" fill="#999b93"> / {total}</tspan></text>
 <text x="90" y="113" textAnchor="middle" fill="#777972" fontSize="10" letterSpacing="2">GATES</text>
 </svg>;
}
export default function Home(){
 const complete=milestones.filter(m=>m.state==="complete").length;
 return <main>
 <header className="site-header"><div className="shell header-inner">
  <a className="brand" href="#top" aria-label="PhysicsResearch home"><span className="brand-glyph">Φ</span><span><strong>PHYSICS<em>RESEARCH</em></strong><small>Independent theoretical inquiry</small></span></a>
  <nav className="top-nav" aria-label="Primary navigation"><a href="#mission">Mission</a><a href="#progress">Progress</a><a href="#laboratory">The laboratory</a><Explorer mode="questionButton"/></nav>
 </div></header>
 <section className="hero shell" id="top"><div className="hero-copy">
   <p className="eyebrow"><span className="eyebrow-line"/>Research programme N° 001 <span className="eyebrow-sep">/</span> Gravity Witness</p>
   <h1>How would we know <i>if gravity is quantum?</i></h1>
   <p className="hero-lede">A carefully documented effort to discover an experiment that can distinguish the quantum nature of gravity from its strongest viable classical alternatives.</p>
   <div className="hero-actions"><a className="primary-link" href="#progress">Explore the research <Arrow/></a><a className="under-link" href={ATLAS} target="_blank" rel="noreferrer">Read the research atlas <Arrow diagonal/></a></div>
   <div className="hero-footnote"><span className="muted-dot"/> RESEARCH STATUS <b>Replication &amp; preliminary design</b><span className="dot-divider">·</span><span>17 OCT 2026 SNAPSHOT</span></div>
  </div><div className="hero-art"><BranchStudy/><div className="art-caption"><span>THE FOUR-PATH EXPERIMENT</span><span>Exhibit I / Conceptual study</span></div></div>
 </section>
 <section id="mission" className="mission-band"><div className="shell mission-grid"><div className="section-side"><span className="section-num">01 / PURPOSE</span><span className="tiny-rule"/></div><div>
  <h2>A precise question. <em>An empirical answer.</em></h2>
  <p>Can a realizable measurement distinguish low-energy quantum gravity from specified classical and hybrid theories, even after accounting for decoherence, experimental noise and competing interactions?</p>
  <p className="mission-note">The aim is not to declare gravity quantum by simulation. It is to identify an observation that could genuinely rule out a competing model.</p>
 </div></div></section>
 <section id="progress" className="shell section-block">
  <div className="section-heading"><div><p className="eyebrow subtle">02 / RESEARCH RECORD</p><h2>Where the evidence stands</h2></div><p className="section-dek">A measured view of progress, not a percentage toward solving fundamental physics.</p></div>
  <div className="evidence-grid">
   <div className="progress-card"><ProgressRing completed={complete} total={milestones.length}/><div><p className="card-kicker">CURRENT POSITION</p><h3>Finite-size tested.<br/>Feasibility unresolved.</h3><p>The equations survive a finite-sphere extension, but our candidate geometry struggles with conducting-shield clearance. Feasibility remains unresolved.</p></div></div>
   <div className="stat-card"><p className="card-kicker">NUMERICAL CHECKS</p><div className="stat-value">{research.testCount.toLocaleString("en-US")}</div><p>Passed in the recorded research suite</p><span>Not mathematical proofs</span></div>
   <div className="stat-card"><p className="card-kicker">FORMAL WORK</p><div className="stat-value">04</div><p>Finite algebra lemmas kernel-checked in Lean</p><span>No claim about the apparatus</span></div>
   <div className="stat-card"><p className="card-kicker">RESEARCH LIBRARY</p><div className="stat-value">{String(research.sourceCount).padStart(2,"0")}</div><p>References catalogued</p><span>{research.claimCount} claims documented · {research.openClaims} open/disputed</span></div>
  </div>
  <div className="milestones"><div className="milestone-head"><h3>Research milestones</h3><span>Evidence-gated · editorially reviewed</span></div>
   {milestones.map(m=><div className={"milestone "+m.state} key={m.number}><span className="milestone-n">{m.number}</span><div className="milestone-content"><h4>{m.title}</h4><p>{m.description}</p></div><span className="milestone-evidence">{m.evidence}</span><span className="milestone-state">{m.state==="complete"?"✓ Complete":m.state==="next"?"Next priority":"Pending"}</span></div>)}
  </div>
 </section>
 <section className="insight-band"><div className="shell insight-grid"><div><p className="eyebrow subtle">03 / INTERPRETATION</p><h2>Entanglement is a <em>clue, not a verdict.</em></h2></div><div>
   <p>Our model predicts a measurable signature in an idealized two-mass system. One restricted classical channel cannot reproduce it; another mathematical countermodel can. Our new constraint audit identifies a severe shielding obstacle, without proving a universal no-go.</p>
   <a href={REPO+"/blob/main/projects/gravity-witness/notes/model_audit.txt"} target="_blank" rel="noreferrer">Inspect the competing models <Arrow diagonal/></a>
 </div></div></section>
 <section className="shell section-block lab-section" id="laboratory"><div className="section-heading"><div><p className="eyebrow subtle">04 / INTERACTIVE STUDY</p><h2>A small virtual laboratory</h2></div><p className="section-dek">Move two assumptions. Watch the predicted quantum witness change. Calculated, not observed.</p></div><Explorer mode="lab" witness={research.witness}/></section>
 <section className="shell resources-section" id="resources"><div className="section-heading"><div><p className="eyebrow subtle">05 / PRIMARY MATERIAL</p><h2>Open the research record</h2></div></div>
 <div className="resource-grid">
  <a href={ATLAS} target="_blank" rel="noreferrer" className="resource-link"><span>01 / READ</span><h3>The living research atlas</h3><p>Accessible explanations, definitions, diagrams and the reasoning behind every gate.</p><b>Google Docs <Arrow diagonal/></b></a>
  <a href={REPO+"/tree/main/projects/gravity-witness"} target="_blank" rel="noreferrer" className="resource-link"><span>02 / REPRODUCE</span><h3>Source &amp; calculations</h3><p>Python simulations, tests, Lean statements, reproducibility records and figures.</p><b>Private GitHub repository <Arrow diagonal/></b></a>
  <a href={REPO+"/blob/main/docs/atlas/2026-10-17-v0.2/atlas.pdf"} target="_blank" rel="noreferrer" className="resource-link"><span>03 / ARCHIVE</span><h3>The illustrated research report</h3><p>A versioned snapshot of the full research atlas, preserved with its figures.</p><b>Atlas PDF <Arrow diagonal/></b></a>
 </div><div className="source-note">Cycle {research.cycle} predictions and Cycle {research.feasibility.phase} constraints, recorded {research.recorded}. Counts come from committed JSON at build time. No experimental data or viability claim. Private resources require permission.</div>
 </section>
 <footer className="site-footer"><div className="shell footer-inner"><div className="footer-brand"><span className="brand-glyph">Φ</span><span>PHYSICSRESEARCH<small>Gravity Witness · An inquiry in progress</small></span></div><div><p>No experimental result. No claim of unification.<br/>A disciplined search for something we can test.</p></div><a href="#top">Back to the beginning ↑</a></div></footer>
 </main>;
}
