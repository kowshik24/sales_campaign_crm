def get_sales_email_template(lead_name):
    company_name = "PetaBytz Technologies Inc."
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{company_name} - Custom Solutions for Your Business</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
            
            body {{
                margin: 0;
                padding: 0;
                font-family: 'Poppins', sans-serif;
                line-height: 1.6;
                color: #333333;
                background-color: #f7f9fc;
            }}
            
            .email-container {{
                max-width: 800px;
                margin: 2rem auto;
                background: white;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                overflow: hidden;
            }}
            
            .header {{
                background: linear-gradient(135deg, #6366f1, #3b82f6);
                padding: 2rem;
                text-align: center;
            }}
            
            .logo {{
                width: 180px;
                margin-bottom: 1rem;
            }}
            
            .content {{
                padding: 2.5rem;
            }}
            
            h1 {{
                color: white;
                margin: 0;
                font-weight: 600;
            }}
            
            h2 {{
                color: #1f2937;
                margin-top: 0;
                font-size: 1.8rem;
            }}
            
            .cta-button {{
                display: inline-block;
                padding: 12px 30px;
                background: #3b82f6;
                color: white !important;
                text-decoration: none;
                border-radius: 8px;
                font-weight: 500;
                margin: 1.5rem 0;
                transition: all 0.3s ease;
                box-shadow: 0 2px 4px rgba(59, 130, 246, 0.3);
            }}
            
            .cta-button:hover {{
                transform: translateY(-2px);
                box-shadow: 0 4px 6px rgba(59, 130, 246, 0.4);
                background: #2563eb;
            }}
            
            .features {{
                display: grid;
                gap: 1.5rem;
                margin: 2rem 0;
            }}
            
            .feature-item {{
                display: flex;
                align-items: center;
                padding: 1.2rem;
                background: #f8fafc;
                border-radius: 8px;
            }}
            
            .feature-icon {{
                font-size: 1.5rem;
                color: #3b82f6;
                margin-right: 1rem;
            }}
            
            .footer {{
                text-align: center;
                padding: 1.5rem;
                background: #f8fafc;
                color: #64748b;
                font-size: 0.9rem;
            }}
            
            @media (max-width: 640px) {{
                .email-container {{
                    margin: 1rem;
                    border-radius: 10px;
                }}
                
                .content {{
                    padding: 1.5rem;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">
                <!-- Replace with actual logo URL -->
                <img src="https://media.licdn.com/dms/image/v2/D560BAQE9Kwch-NT0WQ/company-logo_200_200/company-logo_200_200/0/1665120774767/petabytz_technologies_logo?e=1746662400&v=beta&t=qPPNaY3xAozf-YwmIJc3PnIcOAoXRnw9HoMZMFj55ZQ" alt="{company_name} Logo" class="logo">
                <h1>Transform Your Business with AI Solutions</h1>
            </div>
            
            <div class="content">
                <h2>Hello {lead_name},</h2>
                <p>We're thrilled to connect with you at <strong>{company_name}</strong>! As leaders in enterprise AI solutions, we specialize in helping businesses like yours achieve digital transformation through:</p>
                
                <div class="features">
                    <div class="feature-item">
                        <span class="feature-icon">🚀</span>
                        <div>
                            <strong>Process Automation</strong><br>
                            Streamline operations with intelligent workflows
                        </div>
                    </div>
                    <div class="feature-item">
                        <span class="feature-icon">🤖</span>
                        <div>
                            <strong>Predictive Analytics</strong><br>
                            Make data-driven decisions with AI-powered insights
                        </div>
                    </div>
                    <div class="feature-item">
                        <span class="feature-icon">🔒</span>
                        <div>
                            <strong>Security Solutions</strong><br>
                            Enterprise-grade protection for your digital assets
                        </div>
                    </div>
                </div>

                <p>Let's explore how we can create custom solutions tailored to your specific needs:</p>
                
                <center>
                    <a href="#" class="cta-button">Schedule Your Free Consultation</a>
                </center>

                <p>Why choose {company_name}?</p>
                <ul>
                    <li>✅ 98% Client Satisfaction Rate</li>
                    <li>✅ 24/7 Technical Support</li>
                    <li>✅ Industry-Specific Solutions</li>
                </ul>

                <p>Best Regards,<br>
                <strong>Sarah Johnson</strong><br>
                Director of Business Development<br>
                {company_name}</p>
            </div>
            
            <div class="footer">
                <p>© 2023 {company_name} | 123 Tech Valley, Silicon City, CA 94105</p>
                <p>
                    <a href="#" style="color: #3b82f6; text-decoration: none;">Privacy Policy</a> | 
                    <a href="#" style="color: #3b82f6; text-decoration: none;">Unsubscribe</a>
                </p>
                <div style="margin-top: 1rem;">
                    <a href="#" style="margin: 0 8px;"><img src="https://via.placeholder.com/24.png?text=LI" alt="LinkedIn"></a>
                    <a href="#" style="margin: 0 8px;"><img src="https://via.placeholder.com/24.png?text=TW" alt="Twitter"></a>
                    <a href="#" style="margin: 0 8px;"><img src="https://via.placeholder.com/24.png?text=WB" alt="Website"></a>
                </div>
            </div>
        </div>
    </body>
    </html>
    """