import React from "react";
import { AbsoluteFill } from "remotion";
import { riseStyle, useEnter, WarmBackground } from "../helpers";
import { colors, fonts } from "../theme";

// "Most home care companies send a stranger."
export const Hook: React.FC = () => {
  const line1 = useEnter(8);
  const line2 = useEnter(28);
  const sub = useEnter(95);

  return (
    <AbsoluteFill>
      <WarmBackground base={colors.night} glowA={colors.nightSoft} glowB="#1E1B18" />
      <AbsoluteFill
        style={{
          justifyContent: "center",
          alignItems: "center",
          padding: 140,
          textAlign: "center",
        }}
      >
        <div
          style={{
            fontFamily: fonts.serif,
            fontSize: 92,
            lineHeight: 1.18,
            color: colors.cream,
            maxWidth: 1300,
          }}
        >
          <div style={riseStyle(line1)}>Most home care companies</div>
          <div style={{ ...riseStyle(line2), fontWeight: 600 }}>
            send <span style={{ color: colors.gold, fontStyle: "italic" }}>a stranger.</span>
          </div>
        </div>
        <div
          style={{
            ...riseStyle(sub, 35),
            fontFamily: fonts.sans,
            fontSize: 40,
            color: "#BFB3A6",
            marginTop: 70,
            maxWidth: 1100,
            lineHeight: 1.5,
          }}
        >
          Someone half her age, working a shift.
        </div>
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
