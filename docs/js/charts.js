// XNLP Survey - Charts and Visualizations
// Unified Design System (mohammadi.cv)

// Color palette matching CSS variables
const colors = {
    primary: '#2563eb',
    primaryDark: '#1d4ed8',
    secondary: '#3b82f6',
    accent: '#60a5fa',
    textPrimary: '#1e293b',
    textSecondary: '#64748b',
    // Domain colors
    medicine: '#dc2626',
    finance: '#16a34a',
    social: '#ca8a04',
    crm: '#9333ea',
    reviews: '#0891b2',
    hr: '#ea580c',
    chatbots: '#db2777'
};

// Chart.js global defaults
Chart.defaults.font.family = "'Inter', -apple-system, BlinkMacSystemFont, sans-serif";
Chart.defaults.color = colors.textSecondary;

// Wait for DOM to load
document.addEventListener('DOMContentLoaded', function() {
    // Animate statistics counters
    animateCounters();

    // Initialize charts
    initDomainChart();
    initMethodsChart();
    initRadarChart();
});

// Animate counter numbers
function animateCounters() {
    const counters = document.querySelectorAll('.stat-number');
    const speed = 200;

    const observerOptions = {
        threshold: 0.5
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = +counter.getAttribute('data-target');
                const increment = target / speed;

                const updateCount = () => {
                    const count = +counter.innerText;
                    if (count < target) {
                        counter.innerText = Math.ceil(count + increment);
                        setTimeout(updateCount, 10);
                    } else {
                        counter.innerText = target + '+';
                    }
                };

                updateCount();
                observer.unobserve(counter);
            }
        });
    }, observerOptions);

    counters.forEach(counter => observer.observe(counter));
}

// Domain distribution bar chart
function initDomainChart() {
    const ctx = document.getElementById('domainChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Medicine', 'Finance', 'Social Science', 'CRM', 'Systematic Reviews', 'HR', 'Chatbots'],
            datasets: [{
                label: 'Number of Papers',
                data: [45, 32, 38, 28, 22, 18, 17],
                backgroundColor: [
                    colors.medicine,
                    colors.finance,
                    colors.social,
                    colors.crm,
                    colors.reviews,
                    colors.hr,
                    colors.chatbots
                ],
                borderRadius: 6,
                borderSkipped: false
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: colors.textPrimary,
                    titleColor: '#ffffff',
                    bodyColor: '#ffffff',
                    padding: 12,
                    cornerRadius: 8,
                    titleFont: { size: 14, weight: 600 },
                    bodyFont: { size: 13 }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)',
                        drawBorder: false
                    },
                    ticks: {
                        font: { size: 12 },
                        color: colors.textSecondary
                    }
                },
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        font: { size: 11 },
                        color: colors.textSecondary,
                        maxRotation: 45,
                        minRotation: 45
                    }
                }
            }
        }
    });
}

// XAI Methods horizontal bar chart
function initMethodsChart() {
    const ctx = document.getElementById('methodsChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['SHAP', 'Attention', 'LIME', 'Gradient-based', 'Rule Extraction', 'Rationale Gen.', 'Chain-of-Thought', 'Probing'],
            datasets: [{
                label: 'Usage Frequency',
                data: [85, 78, 72, 45, 38, 35, 28, 22],
                backgroundColor: colors.primary,
                hoverBackgroundColor: colors.primaryDark,
                borderRadius: 6,
                borderSkipped: false
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: colors.textPrimary,
                    titleColor: '#ffffff',
                    bodyColor: '#ffffff',
                    padding: 12,
                    cornerRadius: 8
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)',
                        drawBorder: false
                    },
                    ticks: {
                        font: { size: 12 },
                        color: colors.textSecondary
                    }
                },
                y: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        font: { size: 12 },
                        color: colors.textSecondary
                    }
                }
            }
        }
    });
}

// Domain requirements radar chart
function initRadarChart() {
    const ctx = document.getElementById('radarChart');
    if (!ctx) return;

    new Chart(ctx, {
        type: 'radar',
        data: {
            labels: [
                'Regulatory Compliance',
                'Real-time Requirements',
                'User Trust',
                'Fairness/Bias',
                'Technical Accuracy',
                'Interpretability Depth'
            ],
            datasets: [
                {
                    label: 'Medicine',
                    data: [95, 60, 90, 75, 95, 85],
                    fill: true,
                    backgroundColor: 'rgba(220, 38, 38, 0.1)',
                    borderColor: colors.medicine,
                    borderWidth: 2,
                    pointBackgroundColor: colors.medicine,
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2,
                    pointRadius: 4,
                    pointHoverRadius: 6
                },
                {
                    label: 'Finance',
                    data: [90, 85, 70, 80, 90, 75],
                    fill: true,
                    backgroundColor: 'rgba(22, 163, 74, 0.1)',
                    borderColor: colors.finance,
                    borderWidth: 2,
                    pointBackgroundColor: colors.finance,
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2,
                    pointRadius: 4,
                    pointHoverRadius: 6
                },
                {
                    label: 'HR',
                    data: [85, 40, 75, 95, 70, 80],
                    fill: true,
                    backgroundColor: 'rgba(234, 88, 12, 0.1)',
                    borderColor: colors.hr,
                    borderWidth: 2,
                    pointBackgroundColor: colors.hr,
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2,
                    pointRadius: 4,
                    pointHoverRadius: 6
                },
                {
                    label: 'Chatbots',
                    data: [30, 95, 85, 50, 65, 60],
                    fill: true,
                    backgroundColor: 'rgba(219, 39, 119, 0.1)',
                    borderColor: colors.chatbots,
                    borderWidth: 2,
                    pointBackgroundColor: colors.chatbots,
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2,
                    pointRadius: 4,
                    pointHoverRadius: 6
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: {
                        padding: 20,
                        usePointStyle: true,
                        pointStyle: 'circle',
                        font: { size: 12, weight: 500 },
                        color: colors.textPrimary
                    }
                },
                tooltip: {
                    backgroundColor: colors.textPrimary,
                    titleColor: '#ffffff',
                    bodyColor: '#ffffff',
                    padding: 12,
                    cornerRadius: 8
                }
            },
            scales: {
                r: {
                    min: 0,
                    max: 100,
                    beginAtZero: true,
                    angleLines: {
                        color: 'rgba(0, 0, 0, 0.08)'
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.08)'
                    },
                    pointLabels: {
                        font: { size: 11, weight: 500 },
                        color: colors.textSecondary
                    },
                    ticks: {
                        stepSize: 25,
                        font: { size: 10 },
                        color: colors.textSecondary,
                        backdropColor: 'transparent'
                    }
                }
            }
        }
    });
}

// Copy BibTeX citation
function copyBibtex() {
    const bibtex = document.getElementById('bibtex').innerText;
    const btn = document.querySelector('.copy-btn');

    navigator.clipboard.writeText(bibtex).then(() => {
        btn.textContent = 'Copied!';
        btn.classList.add('copied');

        setTimeout(() => {
            btn.textContent = 'Copy';
            btn.classList.remove('copied');
        }, 2000);
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}
