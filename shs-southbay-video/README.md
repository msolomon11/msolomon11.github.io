# "Someone Who Gets It" — Seniors Helping Seniors South Bay promo video

A 60-second promo (1920×1080 @ 30 fps) built in Remotion. Composition ID:
`SomeoneWhoGetsIt`. Phone and website are props (defaults: `(310) 722-2872`,
`www.southbayshs.com`).

## ⚠️ Missing assets — download before rendering

The scenes reference stock clips and a music track that are NOT committed
(`public/` media is gitignored by size/licensing hygiene). Download free,
commercial-use-licensed assets (Pexels/Pixabay) into these exact paths:

| Path | Scene | What to look for |
|---|---|---|
| `public/footage/hook.mp4` | Hook (0–8s) | Lonely senior at home / unfamiliar caregiver arriving; muted, somber tone |
| `public/footage/peers-coffee.mp4` | Difference | Two seniors laughing over coffee |
| `public/footage/peers-walk.mp4` | Difference | Two seniors walking together outdoors |
| `public/footage/groceries.mp4` | Why it matters | Senior/helper with groceries or cooking together |
| `public/footage/driving.mp4` | Why it matters | Older adults in a car, passenger view, daytime |
| `public/footage/talking.mp4` | Why it matters | Two seniors sitting and talking warmly |
| `public/footage/coast.mp4` | Local | Southern California coastline aerial (Palos Verdes-like) |
| `public/footage/pier.mp4` | Local | Beach pier (Redondo-like), golden hour |
| `public/footage/closing.mp4` | CTA | Warm caregiver-and-client moment, smiles |
| `public/music/bed.mp3` | Whole video | Gentle, warm acoustic/piano bed, ~60s+, uplifting but calm |

Notes:
- Clips are displayed full-bleed under a dark warm scrim (`src/Footage.tsx`),
  so mid-shot, well-lit, low-motion clips read best. Landscape orientation.
- Clips shorter than their scene loop automatically.
- Music loops and has a built-in fade in/out envelope (`src/SomeoneWhoGetsIt.tsx`).

## Commands

```console
npm i                                       # install dependencies
npm run dev                                 # preview in Remotion Studio
npx remotion render SomeoneWhoGetsIt out/someone-who-gets-it.mp4
```

## Sandbox note

`remotion.config.ts` pins the browser to the Claude Code sandbox's
preinstalled Playwright Chromium (`/opt/pw-browsers/...`) and ignores the
sandbox proxy's certificate. Remove those two lines when working locally.
