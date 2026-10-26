let activeCategory = "All";
let searchQuery = "";

const cardsGrid = document.getElementById("cards-grid");
const emptyState = document.getElementById("empty-state");
const searchInput = document.getElementById("search-input");
const categoryButtons = document.querySelectorAll(".filter-btn");
const sortSelect = document.getElementById("sort-select");
const itemModal = document.getElementById("item-modal");
const modalBody = document.getElementById("modal-body");
const closeModalBtn = document.getElementById("close-modal");

function renderItems(items) {
  cardsGrid.innerHTML = "";

  if (items.length === 0) {
    emptyState.classList.remove("hidden");
    return;
  }

  emptyState.classList.add("hidden");

  items.forEach(item => {
    const card = document.createElement("article");
    card.className = "card";
    card.setAttribute("data-id", item.id);

    card.innerHTML = `
      <div class="card-img-container">
        <img src="${item.image}" alt="${item.title}" loading="lazy">
      </div>
      <div class="card-body">
        <div class="card-header-row">
          <span class="card-category">${item.category}</span>
          <span class="card-metric">${item.metric}</span>
        </div>
        <h3 class="card-title">${item.title}</h3>
        <p class="card-description">${item.shortDescription}</p>
      </div>
    `;

    card.addEventListener("click", () => openModal(item));

    cardsGrid.appendChild(card);
  });
}

function filterAndRender() {
  let filtered = catalogItems.filter(item => {
    const matchesCategory = (activeCategory === "All") || (item.category === activeCategory);
    
    const matchesSearch = item.title.toLowerCase().includes(searchQuery) ||
                          item.shortDescription.toLowerCase().includes(searchQuery);

    return matchesCategory && matchesSearch;
  });

  if (sortSelect) {
    const sortValue = sortSelect.value;
    if (sortValue === "title-asc") {
      filtered.sort((a, b) => a.title.localeCompare(b.title));
    } else if (sortValue === "title-desc") {
      filtered.sort((a, b) => b.title.localeCompare(a.title));
    }
  }

  renderItems(filtered);
}

categoryButtons.forEach(button => {
  button.addEventListener("click", () => {
    categoryButtons.forEach(btn => btn.classList.remove("active"));
    button.classList.add("active");

    activeCategory = button.getAttribute("data-category");
    filterAndRender();
  });
});

searchInput.addEventListener("input", (e) => {
  searchQuery = e.target.value.toLowerCase().trim();
  filterAndRender();
});

if (sortSelect) {
  sortSelect.addEventListener("change", filterAndRender);
}

function openModal(item) {
  modalBody.innerHTML = `
    <div style="text-align: center; margin-bottom: 1rem;">
      <img src="${item.image}" alt="${item.title}" style="width: 100%; max-height: 250px; object-fit: cover; border-radius: var(--radius);">
    </div>
    <span class="card-category" style="margin-bottom: 0.5rem; display: inline-block;">${item.category}</span>
    <h2 style="margin-bottom: 0.5rem; font-size: 1.5rem;">${item.title}</h2>
    <p style="font-weight: 600; color: var(--primary-color); margin-bottom: 1rem;">${item.metric}</p>
    <p style="color: var(--text-color); line-height: 1.6;">${item.fullDetails}</p>
  `;

  itemModal.showModal();
}

function closeModal() {
  itemModal.close();
}

closeModalBtn.addEventListener("click", closeModal);

itemModal.addEventListener("click", (e) => {
  const dialogBounds = itemModal.getBoundingClientRect();
  const isClickOutside = (
    e.clientX < dialogBounds.left ||
    e.clientX > dialogBounds.right ||
    e.clientY < dialogBounds.top ||
    e.clientY > dialogBounds.bottom
  );
  
  if (isClickOutside) {
    closeModal();
  }
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && itemModal.open) {
    closeModal();
  }
});

document.addEventListener("DOMContentLoaded", () => {
  renderItems(catalogItems);
});