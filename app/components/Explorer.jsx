"use client";
import { useEffect, useMemo, useState } from "react";

const issueBase = "https://github.com/dhinchcliffe/PhysicsResearch/issues/new";
const contact = "dhinchcliffe@thisisfrontier.ai";

function QuestionPanel({ close }) {
  const [kind,setKind]=useState("Question");
  const [subject,setSubject]=useState("");
  const [message,setMessage]=useState("");
  const [copied,setCopied]=useState(false);
  const draft = `[Gravity Witness / ${kind}] ${subject.trim() || "Untitled inquiry"}\n\n${message.trim()}\n\nContext: Project Gravity Witness research dashboard, Cycle 01.\n`;
  const ready = message.trim().length >= 10;
  const issueUrl = issueBase+"?"+new URLSearchParams({title:kind+": "+(subject.trim()||"Research inquiry"),body:draft}).toString();
  const emailUrl = "mailto:"+contact+"?"+new URLSearchParams({subject:"Gravity Witness — "+(subject.trim()||kind),body:draft}).toString();
  useEffect(()=>{
    function onKey(e){if(e.key==="Escape")close();}
    window.addEventListener("keydown",onKey);
    return ()=>window.removeEventListener("keydown",onKey);
  },[close]);
  async function copy(){try{await navigator.clipboard.writeText(draft);setCopied(true);}catch{setCopied(false);}}
  return <div className="modal-backdrop" onMouseDown={(e)=>{if(e.target===e.currentTarget)close();}}>
    <div className="question-panel" role="dialog" aria-modal="true" aria-labelledby="question-title">
      <div className="panel-top"><span>THE RESEARCH DESK / CORRESPONDENCE</span><button className="close-button" onClick={close} aria-label="Close question form">×</button></div>
      <h2 id="question-title">Every good question moves the work forward.</h2>
      <p>Challenge a model, identify a missing source, or ask for an explanation. This MVP drafts a real email or GitHub issue; it does not silently store a comment.</p>
      <label htmlFor="q-kind">TYPE OF NOTE</label>
      <select id="q-kind" value={kind} onChange={e=>setKind(e.target.value)}><option>Question</option><option>Research comment</option><option>Correction</option><option>Suggested source</option></select>
      <label htmlFor="q-subject">SUBJECT</label>
      <input id="q-subject" value={subject} onChange={e=>setSubject(e.target.value)} maxLength={100} placeholder="The assumption I want to examine…" />
      <label htmlFor="q-body">YOUR NOTE</label>
      <textarea id="q-body" value={message} onChange={e=>{setMessage(e.target.value);setCopied(false);}} maxLength={3000} rows={5} placeholder="What should we investigate or clarify?" />
      <div className="panel-actions">
        <a aria-disabled={!ready} onClick={e=>{if(!ready)e.preventDefault();}} className={"primary-link "+(!ready?"disabled":"")} href={ready?emailUrl:"#"}>Draft email ↗</a>
        <a aria-disabled={!ready} onClick={e=>{if(!ready)e.preventDefault();}} href={ready?issueUrl:"#"} target="_blank" rel="noopener noreferrer" className={"outline-link "+(!ready?"disabled":"")}>Open GitHub issue ↗</a>
        <button disabled={!ready} onClick={copy} className="text-button">{copied?"Copied ✓":"Copy note"}</button>
      </div>
      <p className="panel-small">Email opens your mail application. GitHub submission requires access to our private repository; your text is not sent until you complete that step.</p>
    </div>
  </div>;
}

export default function Explorer({ mode, witness }) {
  const [panel,setPanel]=useState(false);
  const [lambda,setLambda]=useState(witness?.lambda??0.95);
  const [seconds,setSeconds]=useState(witness?.time??2.5);
  const phase = (witness?.phase??-0.3139344923828147) * (seconds/(witness?.time??2.5));
  const score = lambda*lambda+2*lambda*Math.abs(Math.sin(phase/2));
  const crossed = score > (witness?.bound??1);
  const points=useMemo(()=>{
    const f=l=>l*l+2*l*Math.abs(Math.sin(phase/2));
    return Array.from({length:81},(_,i)=>{
      const x=0.6+0.4*i/80;
      return [52+(x-0.6)/0.4*564,242-f(x)/1.6*197];
    });
  },[phase]);
  if(mode==="questionButton") return <>
    <button className="question-button" onClick={()=>setPanel(true)}>Comments &amp; questions <span aria-hidden="true">↗</span></button>
    {panel && <QuestionPanel close={()=>setPanel(false)}/>}
  </>;
  return <div className="lab-card">
    <div className="lab-heading"><div><span className="card-kicker">EXHIBIT 02 / THE ENTANGLEMENT WITNESS</span><h3>What happens when coherence is lost?</h3></div><button className="reset-button" onClick={()=>{setLambda(witness.lambda);setSeconds(witness.time);}}>↺ Reset baseline</button></div>
    <div className="lab-inner">
      <div className="lab-plot">
        <svg viewBox="0 0 680 312" role="img" aria-label="Predicted model witness score as coherence retention changes">
          <g stroke="#dadbd5" strokeWidth="1">
            {[0,0.5,1,1.5].map(y=><line key={y} x1="52" x2="619" y1={242-y/1.6*197} y2={242-y/1.6*197} strokeDasharray={y===1?"7 6":"2 6"}/>)}
          </g>
          <g fill="#777b73" fontSize="12" fontFamily="ui-monospace, monospace">
            {[0,0.5,1,1.5].map(y=><text key={y} x="39" y={246-y/1.6*197} textAnchor="end">{y.toFixed(1)}</text>)}
            {[0.6,0.7,0.8,0.9,1].map(x=><text key={x} x={52+(x-0.6)/0.4*564} y="272" textAnchor="middle">{x.toFixed(1)}</text>)}
            <text x="336" y="300" textAnchor="middle">ASSUMED COHERENCE RETENTION, λ</text>
            <text x="52" y="23">PREDICTED S</text>
          </g>
          <line x1="52" x2="619" y1={242-1/1.6*197} y2={242-1/1.6*197} stroke="#a88069" strokeWidth="1.3" strokeDasharray="6 5"/>
          <text x="614" y={242-1/1.6*197-10} fontSize="11" fill="#986b52" textAnchor="end">separable ceiling = 1</text>
          <path d={points.map((p,i)=>(i?"L":"M")+p[0].toFixed(2)+" "+p[1].toFixed(2)).join(" ")} fill="none" stroke="#304e50" strokeWidth="3" strokeLinecap="round"/>
          <line x1={52+(lambda-.6)/.4*564} x2={52+(lambda-.6)/.4*564} y1="30" y2="243" stroke="#9b5b44" strokeOpacity=".45" strokeDasharray="4 4"/>
          <circle cx={52+(lambda-.6)/.4*564} cy={242-score/1.6*197} r="7" fill="#a45c43" stroke="#fff" strokeWidth="3"/>
        </svg>
        <p className="plot-caption">A hypothetical prediction, not collected data. The retained coherence is an assumed input.</p>
      </div>
      <div className="lab-controls">
        <p className="card-kicker">ADJUST THE ASSUMPTIONS</p>
        <label htmlFor="coherence"><span>Coherence retained</span><strong>{Math.round(lambda*100)}%</strong></label>
        <input id="coherence" type="range" min="0.6" max="1" step="0.005" value={lambda} onChange={e=>setLambda(Number(e.target.value))}/>
        <p className="hint">How much quantum phase information survives the prescribed interaction.</p>
        <label htmlFor="time"><span>Interaction duration</span><strong>{seconds.toFixed(1)} s</strong></label>
        <input id="time" type="range" min="0.5" max="5" step="0.1" value={seconds} onChange={e=>setSeconds(Number(e.target.value))}/>
        <p className="hint">Longer exposure changes the ideal phase, but the toy model holds noise independent of time.</p>
        <div className="lab-readout"><span>Predicted witness S</span><strong>{score.toFixed(3)}</strong><p className={crossed?"crossed":"not-crossed"}>{crossed?"Above separable ceiling in the model":"Below the witness threshold"}</p></div>
      </div>
    </div>
    <div className="lab-footer"><span>MODEL EQUATION <b>S = λ² + 2λ |sin(Δ/2)|</b></span><span>At the original settings: <b>{witness.score.toFixed(3)}</b> (λ = {witness.lambda.toFixed(2)})</span></div>
    <p className="lab-disclaimer"><strong>Interpretation guardrail:</strong> Crossing 1 here means the idealized two-qubit state would be certified as entangled under trusted readout assumptions. It does not demonstrate gravity as the cause or discriminate every classical theory. All controls and physical feasibility remain unverified.</p>
  </div>;
}
