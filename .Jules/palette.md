## 2026-10-29 - Viewport Scalability Anti-pattern
**Learning:** Using `user-scalable=no` or `maximum-scale=1.0` in the viewport meta tag is a severe accessibility issue, particularly for users with low vision who rely on pinch-to-zoom to read content.
**Action:** Always ensure viewport meta tags omit scaling restrictions, leaving only `width=device-width, initial-scale=1.0` to allow native browser zoom functionality.
