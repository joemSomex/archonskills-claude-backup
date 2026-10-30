# Animation stabilization

## Procedure

1. Inspect the actual attachment and identify the action before selecting source frames; it may differ from the most recent deliverable.
2. Use Frame 1 as the alignment reference and preserve it unchanged unless redesign is authorized. Record neck base, chest centerline, stationary shoulders, lower-torso center and main-body bottom crop. Exclude moving hands, hair and detached effects.
3. Match small stable collar, chest and lower-torso patches against Frame 1. Use `cv2.matchTemplate(search_roi, reference_patch, cv2.TM_CCOEFF_NORMED)` with `cv2.minMaxLoc` to measure offsets and scores near the expected locations. Inspect ambiguous matches; measure several heights so a corrected collar cannot conceal a drifting bottom.
4. Correct uniform drift by integer whole-pose registration. If upper and lower offsets disagree, correct the pose rather than stretching the whole character or translating it to satisfy only one landmark. Use local coordinate correction only when the brief permits geometric edits and the result passes native-size anatomy and cluster checks; nearest-neighbor sampling alone does not prove that a warped pose is an acceptable redraw. When the user requires newly drawn in-betweens or forbids warping and patches, redraw complete incompatible poses instead of applying piecewise remaps or transplanting a torso. Reject visible seams, changed pixel density and mismatched perspective.
5. Lock the lower torso crop line AND horizontal torso position to Frame 1. For full-body work, use planted feet. Never center by overall silhouette bounds: raised hands change those bounds without moving the torso. Ignore detached effects when measuring the baseline.
6. Preserve intentional hand gestures, head turns, chin lifts and purposeful bounces. Keep warning/appraisal controlled and move head shakes above a stable torso. Check every transition, including last-to-first, on dark and light mattes.
7. Re-measure upper and lower landmark residuals and verify the common baseline, exact dimensions, RGBA transparency, count and unclipped contours. State measured limitations honestly; equal canvas sizes alone do not demonstrate stability. After adding in-betweens, repeat this check across the complete expanded sequence: a separately generated batch can match the collar while its head is smaller or lower than the approved poses. Measure head geometry independently from torso geometry.
8. Return revised individual PNGs for review before rebuilding a GIF. Save approved original frames separately before alignment or loop-order changes.

## Adding and registering hand-motion in-betweens

- Preserve approved keyframes separately and specify an explicit insertion map before generating additions. For a folded-arm to palm-up gesture, add unfold-near-chest, halfway lift with wrist rotation, and lower/refold poses; keep the opposite arm folded and the moving wrist connected through elbow to shoulder.
- Generate new poses against the approved start, raised-hand, hold and return references together. Review individual PNGs before GIF assembly; a request for previews does not authorize an animated deliverable.
- For small head-size discrepancies in otherwise compatible artwork, detect stable hair features with `cv2.SIFT_create`, ratio-filter descriptor matches and reject outliers with `cv2.estimateAffinePartial2D(..., method=cv2.RANSAC)`. Inspect the inliers: hair features may support registration, but moving brows, eyelids and mouth must not determine the fit.
- Apply any accepted head correction locally, tapering the coordinate displacement to zero before the neck and moving hand. Re-fit scale/translation without rotation when rotation is unintended; never transform the whole figure to repair head proportions. Reject weak or incompatible fits and redraw instead.
- Use nearest-neighbor coordinate remapping rather than blending rendered frames, then inspect neck seams, fingers and pixel clusters. Recheck collar, chest and lower-crop offsets afterward; local head correction must not destabilize the torso. Confirm Frame 1 remains pixel-identical when it is the immutable reference, and check that geometry-only remapping introduces no new RGBA colors.

## Identity and transparency checks

- Preserve moustache, goatee and scars through expressions; parted lips must not erase facial hair.
- Select a chroma key absent from the costume; green can protect purple armor that magenta keying would damage. Inspect enclosed gaps and edge spill, not just corners.
- Lock exact iris base colors through verified iris-only masks. Preserve pupils, glints and shading; verify surrounding pixels unchanged. Do not describe every shaded iris pixel as the identical hex value.
