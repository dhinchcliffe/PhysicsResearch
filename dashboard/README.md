# Gravity Witness dashboard (Vercel MVP)

The repository root now contains a minimal Next.js application for an academic/museum-style research status dashboard. The original Python/Lean research lives **unchanged** in `projects/gravity-witness/`. Installing Node dependencies never installs or invokes the scientific Python environment.

## Local development

Use Node.js 22 or newer and npm, from the **repository root**:

```bash
npm install
npm run dev
```

Open http://localhost:3000. To test the production build:

```bash
npm run build
npm start
```

## Deployment

Import `dhinchcliffe/PhysicsResearch` into Vercel as a **Next.js** project with root directory `.` (repository root). The standard build command is `npm run build`. Vercel requires no dashboard environment variables; a Git-connected project deploys automatically on pushes to the production branch.

## Where the numbers come from

`app/lib/research.js` imports **committed frozen data** directly from:
- `projects/gravity-witness/results/cycle01/cycle01.json`
- `projects/gravity-witness/results/cycle01/dp_reproduction.json`
- `projects/gravity-witness/claims.json`
- `projects/gravity-witness/sources.json`

The dashboard now also reads `projects/gravity-witness/results/cycle02/constraints.json`, `projects/gravity-witness/results/cycle02/claims.json`, and `projects/gravity-witness/results/cycle02/sources.json`. The physical-constraint research gate remains ongoing: geometry and numerical reproducibility do not establish experimental viability.

Test, source and claim counts therefore update at build time when the corresponding records are intentionally updated. Research milestones are manually adjudicated in that module; advancing them is a substantive editorial claim, not a CI run or a percentage toward solving quantum gravity. Cycle 01 values represent simulations under stated idealizations, not observations.

The explorer in `app/components/Explorer.jsx` implements the exact Cycle 01 two-qubit **toy** witness `S = λ² + 2λ|sin(Δ/2)|` and scales the original phase with interaction time. The duration slider is exploratory: it holds coherence constant despite real duration-dependent decoherence and does not represent apparatus feasibility. Always maintain those limitations when extending it.

## Comments & questions

The button opens a functioning note composer with a subject, category and message. **Draft email** opens a local mail app addressed to the published project lead contact; **Open GitHub issue** opens a prefilled issue in this PRIVATE repository and needs collaborator access; **Copy note** copies the same text. The app does not persist comments, claim receipt, require secrets or expose a public write API. A server-side comments inbox is a future enhancement requiring authentication, moderation and storage.

## Security and scope

The dashboard is an informational presentation of selected research records. Do not surface confidential research correspondence, private repository contents or credentials via public routes. The research source files, historical archives and independent Python/Lean CI workflows should remain untouched by dashboard changes.
