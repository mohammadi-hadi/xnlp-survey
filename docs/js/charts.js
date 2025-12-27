// XNLP Survey - Charts and Visualizations

// Color palette
const colors = {
    primary: '#1a365d',
    secondary: '#2c5282',
    accent: '#3182ce',
    medicine: '#e53e3e',
    finance: '#38a169',
    crm: '#805ad5',
    hr: '#dd6b20',
    social: '#d69e2e',
    reviews: '#00b5d8',
    chatbots: '#ed64a6'
};

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
                    backgroundColor: colors.primary,
                    padding: 12,
                    titleFont: { size: 14 },
                    bodyFont: { size: 13 }
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0,0,0,0.05)'
                    },
                    ticks: {
                        font: { size: 12 }
                    }
                },
                x: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        font: { size: 11 },
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
                backgroundColor: colors.accent,
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
                    backgroundColor: colors.primary,
                    padding: 12
                }
            },
            scales: {
                x: {
                    beginAtZero: true,
                    grid: {
                        color: 'rgba(0,0,0,0.05)'
                    },
                    ticks: {
                        font: { size: 12 }
                    }
                },
                y: {
                    grid: {
                        display: false
                    },
                    ticks: {
                        font: { size: 12 }
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
                    backgroundColor: 'rgba(229, 62, 62, 0.1)',
                    borderColor: colors.medicine,
                    pointBackgroundColor: colors.medicine,
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: colors.medicine
                },
                {
                    label: 'Finance',
                    data: [90, 85, 70, 80, 90, 75],
                    fill: true,
                    backgroundColor: 'rgba(56, 161, 105, 0.1)',
                    borderColor: colors.finance,
                    pointBackgroundColor: colors.finance,
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: colors.finance
                },
                {
                    label: 'HR',
                    data: [85, 40, 75, 95, 70, 80],
                    fill: true,
                    backgroundColor: 'rgba(221, 107, 32, 0.1)',
                    borderColor: colors.hr,
                    pointBackgroundColor: colors.hr,
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: colors.hr
                },
                {
                    label: 'Chatbots',
                    data: [30, 95, 85, 50, 65, 60],
                    fill: true,
                    backgroundColor: 'rgba(237, 100, 166, 0.1)',
                    borderColor: colors.chatbots,
                    pointBackgroundColor: colors.chatbots,
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: colors.chatbots
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
                        font: { size: 12 }
                    }
                },
                tooltip: {
                    backgroundColor: colors.primary,
                    padding: 12
                }
            },
            scales: {
                r: {
                    min: 0,
                    max: 100,
                    beginAtZero: true,
                    angleLines: {
                        color: 'rgba(0, 0, 0, 0.1)'
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.1)'
                    },
                    pointLabels: {
                        font: { size: 11 }
                    },
                    ticks: {
                        stepSize: 25,
                        font: { size: 10 },
                        backdropColor: 'transparent'
                    }
                }
            }
        }
    });
}
