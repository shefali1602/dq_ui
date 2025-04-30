// Example: Toggle password visibility (if needed in the future)
function togglePasswordVisibility(fieldId, toggleButtonId) {
    const input = document.getElementById(fieldId);
    const toggle = document.getElementById(toggleButtonId);
    if (input && toggle) {
        input.type = input.type === "password" ? "text" : "password";
        toggle.textContent = input.type === "password" ? "Show Password" : "Hide Password";
    }
}
