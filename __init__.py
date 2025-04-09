from aqt import gui_hooks

# JavaScript to append into Anki's HTML. Iterates through every element of specific classes and replaces their content.
override_due_text = """

<script>
    document.addEventListener("DOMContentLoaded", function() {
        var dues = document.querySelectorAll(".review-count"); 
        for (let x of dues) {
            x.textContent = "!";
            x.style.color = "orange"
        } 
        var finished = document.querySelectorAll(".zero-count"); 
        for (let x of finished) {
            x.textContent = "☑";
        } 
    });
</script>
"""

def inject_deck_browser_hide(deck_browser, content):
    # content.tree += f"{content.tree}"
    # original = """<span class="review-count">"""
    # new = """<span>📑</span><span class="review-count" hidden>"""
    # content.tree = content.tree.replace(original, new)
    content.tree += override_due_text
gui_hooks.deck_browser_will_render_content.append(inject_deck_browser_hide)

def inject_overview_hide(overview, content):
    content.table += override_due_text
gui_hooks.overview_will_render_content.append(inject_overview_hide)