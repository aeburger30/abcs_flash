## 2026-11-02 - Dynamic Content Screen Reader Announcement
**Learning:** When text content updates dynamically (like flashcard letters), screen readers will not announce the new content unless instructed to do so. In an interactive flashcard app, this means users relying on screen readers wouldn't know when the next card appears.
**Action:** Use `aria-live="polite"` and `aria-atomic="true"` on containers whose text content changes dynamically. `polite` ensures the announcement happens naturally without interrupting current speech, and `atomic` ensures the whole content is read.
