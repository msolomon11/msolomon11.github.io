import React from "react";
import { AbsoluteFill, staticFile } from "remotion";
import { Video } from "@remotion/media";
import { linearTiming, TransitionSeries } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";

// Full-bleed stock clip with a warm dark scrim for text legibility
export const Footage: React.FC<{ src: string; scrim?: number }> = ({
  src,
  scrim = 0.62,
}) => (
  <AbsoluteFill>
    <Video
      muted
      loop
      src={staticFile(src)}
      style={{ width: "100%", height: "100%", objectFit: "cover" }}
    />
    <AbsoluteFill
      style={{
        background: `linear-gradient(180deg, rgba(32,26,21,${Math.max(
          scrim - 0.15,
          0,
        )}) 0%, rgba(32,26,21,${scrim}) 75%)`,
      }}
    />
  </AbsoluteFill>
);

// Several clips cut together with crossfades, used as a scene background
export const FootageCuts: React.FC<{
  clips: { src: string; durationInFrames: number }[];
  scrim?: number;
}> = ({ clips, scrim }) => (
  <AbsoluteFill>
    <TransitionSeries>
      {clips.flatMap((clip, i) => [
        ...(i > 0
          ? [
              <TransitionSeries.Transition
                key={`t-${i}`}
                presentation={fade()}
                timing={linearTiming({ durationInFrames: 15 })}
              />,
            ]
          : []),
        <TransitionSeries.Sequence
          key={clip.src}
          durationInFrames={clip.durationInFrames}
        >
          <Footage src={clip.src} scrim={scrim} />
        </TransitionSeries.Sequence>,
      ])}
    </TransitionSeries>
  </AbsoluteFill>
);
