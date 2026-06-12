import React from "react";
import { AbsoluteFill } from "remotion";
import { Kicker, riseStyle, useEnter } from "../helpers";
import { FootageCuts } from "../Footage";
import { colors, fonts } from "../theme";

const SERVICES = [
  "Meals",
  "Errands",
  "Rides to the doctor",
  "A hand around the house",
  "Real conversation",
];

const Chip: React.FC<{ label: string; delay: number }> = ({ label, delay }) => {
  const progress = useEnter(delay, 25);
  return (
    <div
      style={{
        ...riseStyle(progress, 35),
        fontFamily: fonts.sans,
        fontSize: 38,
        fontWeight: 600,
        color: colors.ink,
        background: "#FAF4EAE6",
        borderRadius: 999,
        padding: "22px 48px",
        boxShadow: "0 10px 30px rgba(0, 0, 0, 0.25)",
      }}
    >
      {label}
    </div>
  );
};

// "Care that feels like company." over groceries / driving / talking cuts
export const WhyItMatters: React.FC = () => {
  const headline = useEnter(25);
  const sub = useEnter(70);

  return (
    <AbsoluteFill>
      <FootageCuts
        clips={[
          { src: "footage/groceries.mp4", durationInFrames: 145 },
          { src: "footage/driving.mp4", durationInFrames: 145 },
          { src: "footage/talking.mp4", durationInFrames: 150 },
        ]}
      />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          padding: 140,
          textAlign: "center",
          gap: 52,
        }}
      >
        <Kicker delay={10} color={colors.gold}>
          Why it matters
        </Kicker>
        <div
          style={{
            ...riseStyle(headline),
            fontFamily: fonts.serif,
            fontWeight: 600,
            fontSize: 110,
            lineHeight: 1.15,
            color: colors.creamText,
            maxWidth: 1350,
          }}
        >
          Care that feels like <span style={{ color: colors.gold, fontStyle: "italic" }}>company.</span>
        </div>
        <div
          style={{
            ...riseStyle(sub, 35),
            fontFamily: fonts.sans,
            fontSize: 42,
            color: colors.creamSoft,
            maxWidth: 1150,
            lineHeight: 1.5,
          }}
        >
          It&rsquo;s not a transaction. It&rsquo;s a friendship with help built in.
        </div>
        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            justifyContent: "center",
            gap: 28,
            maxWidth: 1450,
            marginTop: 20,
          }}
        >
          {SERVICES.map((label, i) => (
            <Chip key={label} label={label} delay={130 + i * 16} />
          ))}
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
