document.addEventListener('DOMContentLoaded', function () {
    // Auto-scroll to main content on load
    const contentBlock = document.getElementById("main-content");
    if (contentBlock) {
      contentBlock.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  
    // Initialize Choices.js for Project ID dropdown
    const dropdown = document.querySelector('#projectDropdown');
    if (dropdown) {
      new Choices(dropdown, {
        searchEnabled: true,
        shouldSort: false,
        itemSelectText: '',
        placeholder: true,
        placeholderValue: 'Click here to Select Project ID',
      });
    }
  
    // Override search box placeholder inside dropdown (Choices.js internal)
    const observer = new MutationObserver(() => {
      const searchInput = document.querySelector('.choices__input.choices__input--cloned');
      if (searchInput && !searchInput.placeholder) {
        searchInput.placeholder = 'search project id';
      }
    });
  
    observer.observe(document.body, { childList: true, subtree: true });
  });

  function toggleDsSource() {
    const section = document.getElementById("dsSourceSection");
    const btn = document.querySelector(".ds-source-toggle button");
  
    if (section.style.display === "none" || section.style.display === "") {
      section.style.display = "flex";
      btn.textContent = "DS_Source ▼";
    } else {
      section.style.display = "none";
      btn.textContent = "DS_Source ▶";
    }
  }