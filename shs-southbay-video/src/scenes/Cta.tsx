import React from "react";
import { AbsoluteFill } from "remotion";
import { Kicker, riseStyle, useEnter } from "../helpers";
import { Footage } from "../Footage";
import { colors, fonts } from "../theme";
import type { ContactProps } from "../props";

// "If your parent needs help at home..." over a warm closing shot
export const Cta: React.FC<ContactProps> = ({ phone, website }) => {
  const headline = useEnter(20);
  const phoneIn = useEnter(80);
  const siteIn = useEnter(105);
  const sub = useEnter(140);

  return (
    <AbsoluteFill>
      <Footage src="footage/closing.mp4" scrim={0.68} />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          padding: 140,
          textAlign: "center",
          gap: 50,
        }}
      >
        <Kicker delay={5} color={colors.gold}>
          If your parent needs help at home
        </Kicker>
        <div
          style={{
            ...riseStyle(headline),
            fontFamily: fonts.serif,
            fontWeight: 600,
            fontSize: 96,
            lineHeight: 1.2,
            color: colors.creamText,
            maxWidth: 1350,
          }}
        >
          They deserve more than{" "}
          <span style={{ color: colors.gold, fontStyle: "italic" }}>
            a stranger on a shift.
          </span>
        </div>
        <div
          style={{
            ...riseStyle(phoneIn, 40),
            fontFamily: fonts.sans,
            fontWeight: 700,
            fontSize: 110,
            color: colors.gold,
            letterSpacing: "0.02em",
            marginTop: 24,
          }}
        >
          {phone}
        </div>
        <div
          style={{
            ...riseStyle(siteIn, 30),
            fontFamily: fonts.sans,
            fontWeight: 600,
            fontSize: 52,
            color: colors.creamText,
          }}
        >
          {website}
        </div>
        <div
          style={{
            ...riseStyle(sub, 30),
            fontFamily: fonts.sans,
            fontSize: 38,
            color: colors.creamSoft,
            lineHeight: 1.5,
            maxWidth: 1350,
          }}
        >
          The first conversation is free — and it&rsquo;s with a real person who
          lives here.
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
