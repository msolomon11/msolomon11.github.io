import React from "react";
import { AbsoluteFill } from "remotion";
import { riseStyle, useEnter, WarmBackground } from "../helpers";
import { colors, fonts } from "../theme";
import { PeerMark } from "./Difference";
import type { ContactProps } from "../props";

// Logo card: "Care from someone who gets it."
export const EndCard: React.FC<ContactProps> = ({ phone, website }) => {
  const brand = useEnter(12);
  const tagline = useEnter(40);
  const contact = useEnter(60);

  return (
    <AbsoluteFill>
      <WarmBackground />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          textAlign: "center",
          gap: 44,
        }}
      >
        <PeerMark delay={0} size={100} />
        <div style={riseStyle(brand)}>
          <div
            style={{
              fontFamily: fonts.serif,
              fontWeight: 600,
              fontSize: 84,
              color: colors.ink,
            }}
          >
            Seniors Helping Seniors®
          </div>
          <div
            style={{
              fontFamily: fonts.sans,
              fontWeight: 700,
              fontSize: 40,
              letterSpacing: "0.35em",
              textTransform: "uppercase",
              color: colors.terracotta,
              marginTop: 14,
            }}
          >
            South Bay
          </div>
        </div>
        <div
          style={{
            ...riseStyle(tagline, 30),
            fontFamily: fonts.serif,
            fontStyle: "italic",
            fontSize: 52,
            color: colors.inkSoft,
          }}
        >
          Care from someone who gets it.
        </div>
        <div
          style={{
            ...riseStyle(contact, 25),
            fontFamily: fonts.sans,
            fontWeight: 600,
            fontSize: 40,
            color: colors.ink,
            display: "flex",
            gap: 36,
            alignItems: "center",
          }}
        >
          <span>{phone}</span>
          <span style={{ color: colors.gold }}>·</span>
          <span>{website}</span>
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
