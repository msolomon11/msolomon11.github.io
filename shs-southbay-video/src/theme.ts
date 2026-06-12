import { loadFont as loadFraunces } from "@remotion/google-fonts/Fraunces";
import { loadFont as loadSourceSans } from "@remotion/google-fonts/SourceSans3";

const fraunces = loadFraunces("normal", {
  weights: ["400", "600"],
  subsets: ["latin"],
});

const sourceSans = loadSourceSans("normal", {
  weights: ["400", "600", "700"],
  subsets: ["latin"],
});

export const fonts = {
  serif: fraunces.fontFamily,
  sans: sourceSans.fontFamily,
};

export const colors = {
  cream: "#FAF4EA",
  // Light text for use over footage scrims
  creamText: "#F7EFE3",
  creamSoft: "#D8CBBA",
  creamDark: "#F1E6D4",
  ink: "#3B2E25",
  inkSoft: "#6B5B4E",
  terracotta: "#C2553D",
  gold: "#E0A458",
  sage: "#7C8C6F",
  night: "#2B2723",
  nightSoft: "#4A4239",
};
