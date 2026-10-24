## 2026-10-24 - Dynamic Mute Button Attributes
**Learning:** Screen reader users rely heavily on `aria-label` attributes for icon-only buttons. We found that the `toggleMute` function successfully updated visual states but failed to update the `aria-label` and `title` tags dynamically when mute was enabled, confusing screen reader users.
**Action:** Always ensure that `aria-label` and `title` tags are updated synchronously with visual and functional state changes for buttons.
