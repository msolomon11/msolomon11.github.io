import React from "react";
import { linearTiming, TransitionSeries } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { Hook } from "./scenes/Hook";
import { Difference } from "./scenes/Difference";
import { WhyItMatters } from "./scenes/WhyItMatters";
import { Local } from "./scenes/Local";
import { Cta } from "./scenes/Cta";
import { EndCard } from "./scenes/EndCard";
import type { ContactProps } from "./props";

const TRANSITION = 20;

export const SCENE_DURATIONS = {
  hook: 260,
  difference: 380,
  why: 380,
  local: 380,
  cta: 380,
  endCard: 120,
};

// Total = sum of scenes - 5 overlapping transitions = 1800 frames (60s @ 30fps)
export const TOTAL_DURATION =
  Object.values(SCENE_DURATIONS).reduce((a, b) => a + b, 0) - 5 * TRANSITION;

const crossfade = () => (
  <TransitionSeries.Transition
    presentation={fade()}
    timing={linearTiming({ durationInFrames: TRANSITION })}
  />
);

export const SomeoneWhoGetsIt: React.FC<ContactProps> = ({ phone, website }) => {
  return (
    <TransitionSeries>
      <TransitionSeries.Sequence durationInFrames={SCENE_DURATIONS.hook}>
        <Hook />
      </TransitionSeries.Sequence>
      {crossfade()}
      <TransitionSeries.Sequence durationInFrames={SCENE_DURATIONS.difference}>
        <Difference />
      </TransitionSeries.Sequence>
      {crossfade()}
      <TransitionSeries.Sequence durationInFrames={SCENE_DURATIONS.why}>
        <WhyItMatters />
      </TransitionSeries.Sequence>
      {crossfade()}
      <TransitionSeries.Sequence durationInFrames={SCENE_DURATIONS.local}>
        <Local />
      </TransitionSeries.Sequence>
      {crossfade()}
      <TransitionSeries.Sequence durationInFrames={SCENE_DURATIONS.cta}>
        <Cta phone={phone} website={website} />
      </TransitionSeries.Sequence>
      {crossfade()}
      <TransitionSeries.Sequence durationInFrames={SCENE_DURATIONS.endCard}>
        <EndCard phone={phone} website={website} />
      </TransitionSeries.Sequence>
    </TransitionSeries>
  );
};
