import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { easeInOut, Kicker, riseStyle, useEnter } from "../helpers";
import { FootageCuts } from "../Footage";
import { colors, fonts } from "../theme";

const PLACES = ["Torrance", "Redondo Beach", "Palos Verdes", "The Beach Cities"];

// A coastline stroke that draws itself across the screen
const Coastline: React.FC<{ delay: number }> = ({ delay }) => {
  const frame = useCurrentFrame();
  const length = 2000;
  const drawn = interpolate(frame, [delay, delay + 80], [length, 0], {
    easing: easeInOut,
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <svg
      width={1400}
      height={120}
      viewBox="0 0 1400 120"
      style={{ overflow: "visible" }}
    >
      <path
        d="M 0 70 C 180 20, 320 110, 500 60 S 850 10, 1020 70 S 1300 110, 1400 50"
        fill="none"
        stroke={colors.gold}
        strokeWidth={7}
        strokeLinecap="round"
        strokeDasharray={length}
        strokeDashoffset={drawn}
        opacity={0.9}
      />
    </svg>
  );
};

const Place: React.FC<{ label: string; delay: number }> = ({ label, delay }) => {
  const progress = useEnter(delay, 25);
  return (
    <div
      style={{
        ...riseStyle(progress, 30),
        display: "flex",
        alignItems: "center",
        gap: 18,
        fontFamily: fonts.sans,
        fontSize: 44,
        fontWeight: 600,
        color: colors.creamText,
      }}
    >
      <div
        style={{
          width: 16,
          height: 16,
          borderRadius: "50%",
          background: colors.gold,
        }}
      />
      {label}
    </div>
  );
};

// "Locally owned. Licensed. South Bay." over coastline footage
export const Local: React.FC = () => {
  const headline = useEnter(25);
  const sub = useEnter(75);

  return (
    <AbsoluteFill>
      <FootageCuts
        clips={[
          { src: "footage/coast.mp4", durationInFrames: 205 },
          { src: "footage/pier.mp4", durationInFrames: 190 },
        ]}
      />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          padding: 140,
          textAlign: "center",
          gap: 50,
        }}
      >
        <Kicker delay={10} color={colors.gold}>
          Locally owned · State-licensed
        </Kicker>
        <div
          style={{
            ...riseStyle(headline),
            fontFamily: fonts.serif,
            fontWeight: 600,
            fontSize: 120,
            color: colors.creamText,
          }}
        >
          We&rsquo;re your <span style={{ color: colors.gold, fontStyle: "italic" }}>neighbors.</span>
        </div>
        <div
          style={{
            ...riseStyle(sub, 35),
            fontFamily: fonts.sans,
            fontSize: 42,
            color: colors.creamSoft,
            maxWidth: 1450,
            lineHeight: 1.5,
          }}
        >
          Not a national call center — South Bay families, served by South Bay
          people.
        </div>
        <Coastline delay={100} />
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            gap: 70,
            flexWrap: "wrap",
          }}
        >
          {PLACES.map((label, i) => (
            <Place key={label} label={label} delay={130 + i * 18} />
          ))}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
