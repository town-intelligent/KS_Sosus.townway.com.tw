import os

file_list = [
    "ab_cms_personal_file.html", 
    "ab_contact_person.html", 
    "ab_project_planning.html", 
    "admin_agent_message_list.html", 
    "admin_local.html", 
    "cms_ab.html", 
    "ab_cms_project_detail.html", 
    "ab_my_project.html", 
    "ab_sdgs_setting.html", 
    "admin_dashboard.html", 
    "admin_message_list.html", 
    "ab_cms_submit_form.html", 
    "ab_plan_info.html", 
    "admin_agent.html", 
    "admin_enterprise.html", 
    "admin_project.html"
]


image_list = [
    "2nd-home-news.png",
    "2nd-home.png",
    "5-ways-of-life-chart.png",
    "ab_cms_project_detail.png",
    "about-2nd-home.png",
    "ab_project_detail.png",
    "agent_chart.png",
    "agent_foot_print.png",
    "banner-contact-us.png",
    "bar_chart.svg",
    "blockchain.svg",
    "chart_2.jpg",
    "cms_contact_us_banner.png",
    "community -development-chart.png",
    "countryside-revitalization-icon.png",
    "dashboard-icon.png",
    "delete-icon.svg",
    "ditital_twins.png",
    "edit.svg",
    "enterprise.svg",
    "fbLogo.svg",
    "footer-decoration.svg",
    "footprint.jpg",
    "forward_to_inbox.svg",
    "handshake.svg",
    "igLogo.svg",
    "linkedinLogo.svg",
    "local.svg",
    "place-marker.svg",
    "product.jpg",
    "product.png",
    "project-chart.png",
    "project-img-02.png",
    "project_img_02.png",
    "project_img_03.png",
    "project-img-04.png",
    "project_img_04.png",
    "project-img.jpg",
    "project_img.jpg",
    "SDGs_All_Logo.png",
    "SDGs_all.png",
    "SDGs_Chart.jpg",
    "SDGs-chart.png",
    "SDGs_Circle.png",
    "sns-person-icon.png",
    "SOLUTION.jpg",
    "startup-rocket-icon.png",
    "sustainable-enterprise-icon.png",
    "T-Planet-architecture-Tc-s.jpg",
    "tplanet_map.png",
    "upload-icon.png",
    "youtubeLogo.svg"
]

# Remove the file of the list
for file in file_list:
    if os.path.exists(file):
        os.remove(file)
        print("The file " , file, "has been removed.")
    elif os.path.exists("backend/" + file):
        os.remove("backend/" + file)
        print("The file backend/" , file, "has been removed.")
    else:
        print("The filename " , file, " does not exist.")

# Remove the image of the list
for image in image_list:
    if os.path.exists("static/imgs/" + image):
        os.remove("static/imgs/" + image)
        print("The image " , image, "has been removed.")
    else:
        print("The image " , image, " does not exist.")


copy_list = [
    "tplanet_map.png",
    "2nd-home-contact-us.png",
    "project_img_03.png",
    "project_img.jpg",
    "2nd-home-csr.png",
    "news1.jpg",
    "news2.jpg",
    "news3.jpg",
    "news4.jpg",
    "news5.jpg",
    "news6.jpg",
    "csr.png",
    "2nd-home-solution.png",
    "news-banner.jpg"
]

source_dir = "/home/yillkid/workspace/town-intelligent-alpha/tplanet.townway.com.tw/static/imgs/"
target_dir = "static/imgs/"

import shutil
for file_name in copy_list:
    source_file = os.path.join(source_dir, file_name)
    target_file = os.path.join(target_dir, file_name)
    if os.path.exists(source_file):
        shutil.copy(source_file, target_file)
        print(f"Copied {source_file} to {target_file}")
    else:
        print(f"{source_file} does not exist")