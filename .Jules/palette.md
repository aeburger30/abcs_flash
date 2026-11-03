## 2024-11-03 - Dynamic Flashcard Accessibility
**Learning:** For static flashcard applications where the main content updates dynamically without a page refresh, screen readers might not announce the new content automatically.
**Action:** Use the `aria-live="polite"` and `aria-atomic="true"` attributes on the container displaying the changing content to ensure screen readers announce updates smoothly and completely.
