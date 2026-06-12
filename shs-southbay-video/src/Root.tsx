import "./index.css";
import { Composition } from "remotion";
import { SomeoneWhoGetsIt, TOTAL_DURATION } from "./SomeoneWhoGetsIt";
import { defaultContact } from "./props";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="SomeoneWhoGetsIt"
        component={SomeoneWhoGetsIt}
        durationInFrames={TOTAL_DURATION}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={defaultContact}
      />
    </>
  );
};
