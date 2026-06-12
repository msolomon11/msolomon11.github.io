import React from "react";
import { AbsoluteFill, Easing, interpolate, useCurrentFrame } from "remotion";
import { colors } from "./theme";

export const easeOut = Easing.bezier(0.16, 1, 0.3, 1);
export const easeInOut = Easing.bezier(0.45, 0, 0.55, 1);

export const useEnter = (delay: number, duration = 30) => {
  const frame = useCurrentFrame();
  return interpolate(frame, [delay, delay + duration], [0, 1], {
    easing: easeOut,
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
};

export const riseStyle = (progress: number, distance = 50): React.CSSProperties => ({
  opacity: progress,
  transform: `translateY(${(1 - progress) * distance}px)`,
});

// Slow-drifting warm radial gradients used behind every scene
export const WarmBackground: React.FC<{
  base?: string;
  glowA?: string;
  glowB?: string;
}> = ({ base = colors.cream, glowA = colors.gold, glowB = colors.terracotta }) => {
  const frame = useCurrentFrame();
  const drift = interpolate(frame, [0, 600], [0, 1], {
    extrapolateRight: "clamp",
    easing: easeInOut,
  });
  const x1 = interpolate(drift, [0, 1], [18, 28]);
  const y1 = interpolate(drift, [0, 1], [22, 30]);
  const x2 = interpolate(drift, [0, 1], [85, 75]);
  const y2 = interpolate(drift, [0, 1], [80, 70]);

  return (
    <AbsoluteFill
      style={{
        background: `
          radial-gradient(900px 700px at ${x1}% ${y1}%, ${glowA}33, transparent 70%),
          radial-gradient(1000px 800px at ${x2}% ${y2}%, ${glowB}26, transparent 70%),
          ${base}`,
      }}
    />
  );
};

export const Kicker: React.FC<{
  children: React.ReactNode;
  delay?: number;
  color?: string;
}> = ({ children, delay = 0, color = colors.terracotta }) => {
  const progress = useEnter(delay);
  return (
    <div
      style={{
        ...riseStyle(progress, 30),
        fontSize: 30,
        fontWeight: 700,
        letterSpacing: "0.22em",
        textTransform: "uppercase",
        color,
      }}
    >
      {children}
    </div>
  );
};
