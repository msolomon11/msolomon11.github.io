import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { easeOut, Kicker, riseStyle, useEnter } from "../helpers";
import { FootageCuts } from "../Footage";
import { colors, fonts } from "../theme";

// Two circles drifting together — the peer-to-peer mark
export const PeerMark: React.FC<{
  delay?: number;
  size?: number;
  onDark?: boolean;
}> = ({ delay = 0, size = 120, onDark = false }) => {
  const frame = useCurrentFrame();
  const join = interpolate(frame, [delay, delay + 45], [0, 1], {
    easing: easeOut,
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const gap = interpolate(join, [0, 1], [size * 0.9, size * 0.32]);

  return (
    <div
      style={{
        position: "relative",
        width: size * 2,
        height: size,
        opacity: join,
      }}
    >
      <div
        style={{
          position: "absolute",
          top: 0,
          left: size - gap,
          width: size,
          height: size,
          borderRadius: "50%",
          background: colors.terracotta,
          mixBlendMode: onDark ? "normal" : "multiply",
          opacity: onDark ? 0.92 : 1,
        }}
      />
      <div
        style={{
          position: "absolute",
          top: 0,
          right: size - gap,
          width: size,
          height: size,
          borderRadius: "50%",
          background: colors.gold,
          mixBlendMode: onDark ? "normal" : "multiply",
          opacity: onDark ? 0.92 : 1,
        }}
      />
    </div>
  );
};

// "We send a peer."
export const Difference: React.FC = () => {
  const headline = useEnter(30);
  const body = useEnter(110);

  return (
    <AbsoluteFill>
      <FootageCuts
        clips={[
          { src: "footage/peers-coffee.mp4", durationInFrames: 205 },
          { src: "footage/peers-walk.mp4", durationInFrames: 190 },
        ]}
      />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          padding: 140,
          textAlign: "center",
          gap: 56,
        }}
      >
        <PeerMark delay={10} onDark />
        <Kicker delay={20} color={colors.gold}>
          Seniors Helping Seniors® South Bay
        </Kicker>
        <div
          style={{
            ...riseStyle(headline),
            fontFamily: fonts.serif,
            fontWeight: 600,
            fontSize: 130,
            color: colors.creamText,
          }}
        >
          We send <span style={{ color: colors.gold, fontStyle: "italic" }}>a peer.</span>
        </div>
        <div
          style={{
            ...riseStyle(body, 35),
            fontFamily: fonts.sans,
            fontSize: 42,
            lineHeight: 1.5,
            color: colors.creamSoft,
            maxWidth: 1250,
          }}
        >
          Our caregivers are seniors themselves — active, capable, and at a stage
          of life where they understand what your parent is going through.
          Because they&rsquo;re living it too.
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
