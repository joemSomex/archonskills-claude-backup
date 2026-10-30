# Cinematic Video Prompt Craft Guide

Use this reference when a task needs detailed shot construction. Apply only the dimensions relevant to the requested model and clip; more detail is not automatically better.

## Scene-to-shot translation

Translate each narrative beat into observable evidence:

- **Thought or realization:** gaze settles on evidence, breathing changes, posture stills, response is delayed, delivery changes.
- **Fear:** guarded distance, interrupted movement, shallow breath, attention fixed on the threat; avoid generic trembling unless supported.
- **Authority:** economical movement, stable eyeline, unhurried cadence, controlled use of space.
- **Deception:** mismatch between reassuring words and guarded behavior, a withheld reaction, strategic redirection.
- **Decision:** a clear pause followed by committed movement or speech.
- **Relationship shift:** changed proximity, touch, eyeline, interruption pattern, or willingness to turn away.

Do not claim the model can render hidden backstory, symbolic intent, or internal narration unless voice-over, text, or an observable device communicates it.

## Prompt construction order

A reliable prompt usually benefits from this order, adjusted to the platform:

1. State clip type, duration, aspect ratio, and overall visual intent when known.
2. Anchor the subject identities and immutable appearance details.
3. Establish the environment, time, atmosphere, and spatial layout.
4. State the opening composition and camera position.
5. Describe action chronologically in a few clear beats.
6. Direct the performance and dialogue at the moment they occur.
7. Describe camera movement motivated by the action.
8. State lighting, sound, and finishing texture that materially affect the shot.
9. Lock the final frame or handoff state.
10. Add a short failure-prevention block only where needed.

Keep each instruction compatible with the others. Avoid multiple simultaneous camera moves, mutually exclusive framings, or a subject performing more actions than the duration permits.

## Camera direction

Choose camera language for narrative function:

- **Locked or nearly locked frame:** tension, observation, restraint, or performance-led dialogue.
- **Slow push-in:** increasing recognition or pressure; do not use automatically for every emotional line.
- **Pull-back:** isolation, revelation of scale, or emotional separation.
- **Tracking movement:** pursuit, discovery through space, or sustained physical intent.
- **Handheld:** instability or immediacy when the world supports it; avoid using it as shorthand for intensity.
- **Reveal pan or tilt:** disclose information the subject or audience discovers in sequence.
- **Cut or shot split:** use when a single continuous move would hide causality or exceed duration.

State framing and movement plainly. If a reference frame governs composition, describe only the intended motion and changes rather than re-inventing the still image.

## Blocking and action

Track where each subject starts, what they touch, how they cross the space, and where they finish. Preserve object possession and screen direction. Use ordered beats instead of disconnected visual adjectives.

Prefer one primary action and one reaction per short clip. For complex action, divide into setup, escalation, impact, and aftermath shots. Make impacts and environmental reactions physically causal.

## Performance direction

Direct the playable intention first, then add minimal observable signals:

- objective: what the character wants in the moment;
- pressure: what makes that difficult;
- mask: what the character is trying not to reveal;
- restraint: understated, natural, heightened, exhausted, formal, or volatile;
- signals: one or two choices in gaze, breath, posture, distance, gesture, or vocal rhythm.

Avoid exhaustive facial choreography, repeated emotional synonyms, and contradictory directions such as calm panic or motionless pacing unless the contradiction is intentionally explained.

## Dialogue and voice

Preserve exact dialogue when supplied. Name the speaker before the line and keep turn order unambiguous. Specify whether speech is on-camera, off-screen, voice-over, whispered, interrupted, or overlapping only when relevant.

Describe voice with supported attributes: age, register, texture, energy, pace, volume, accent, articulation, emotional pressure, and breath. Never infer an accent from ethnicity, nationality, costume, or archetype. When reference audio exists, defer to it rather than approximating from text.

Allow silence and reaction time. A line, a breath, and a look may need more screen time than their word count suggests.

## Environment, light, and sound

Use environmental details that affect action, visibility, mood, scale, or continuity. Keep architecture and geography stable. Distinguish atmosphere from weather and practical light from stylistic grading.

Tie lighting to sources when possible: window light, signage, fire, overhead fixtures, moonlight, vehicle lamps. Avoid simultaneously demanding incompatible times of day or light directions.

Include sound cues that carry story information: a distant impact, failing machinery, fabric movement, footsteps, room tone, an interrupted signal. Do not overload the prompt with a full sound mix unless the generation system supports it.

## Timing

Budget duration by action rather than prose length. Account for establishing, movement, dialogue, reaction, and final hold. For short generations, prioritize one emotional turn. Split a sequence when it contains multiple locations, complex choreography, several dialogue exchanges, or a major transformation followed by extended aftermath.

## Negative constraints

Use negatives to protect identity, anatomy, continuity, dialogue ownership, camera behavior, text rendering, and known model failure modes. Keep them short and specific. Prefer a strong positive instruction over a broad prohibition.

Examples of useful constraints:

- preserve the supplied face, costume, and eye colour;
- no extra characters or duplicated limbs;
- no unscripted dialogue; preserve synchronized lip movement only for approved on-camera speech;
- no camera cut; maintain the continuous take;
- do not alter the reference environment;
- keep the named object in the same hand.

## Revision comparison

For a surgical revision, compare old and new prompts under these headings:

- requested change;
- intentionally changed text;
- preserved locks;
- continuity consequences;
- accidental differences to revert.

Do not report a surgical revision as complete until accidental differences are removed.
