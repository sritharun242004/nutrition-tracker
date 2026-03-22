// Toggle password visibility
function togglePassword(inputId, btn) {
  const input = document.getElementById(inputId);
  const icon = btn.querySelector('i');
  if (input.type === 'password') {
    input.type = 'text';
    icon.className = 'bi bi-eye-slash';
  } else {
    input.type = 'password';
    icon.className = 'bi bi-eye';
  }
}

// Auto-dismiss alerts after 5 seconds
document.addEventListener('DOMContentLoaded', function () {
  const alerts = document.querySelectorAll('.alert.alert-dismissible');
  alerts.forEach(function (alert) {
    setTimeout(function () {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      if (bsAlert) bsAlert.close();
    }, 5000);
  });

  // Activate tooltips
  const tooltipTriggers = document.querySelectorAll('[data-bs-toggle="tooltip"]');
  tooltipTriggers.forEach(function (el) {
    new bootstrap.Tooltip(el);
  });

  // Live calorie calculation when quantity changes in log food form
  const qtyInput = document.querySelector('input[name="quantity"]');
  if (qtyInput) {
    qtyInput.addEventListener('input', function () {
      const qty = parseFloat(this.value) || 100;
      const calPer100 = parseFloat(this.dataset.calPer100 || 0);
      const calDisplay = document.getElementById('calDisplay');
      if (calDisplay && calPer100) {
        calDisplay.textContent = Math.round(calPer100 * qty / 100) + ' kcal';
      }
    });
  }
});
