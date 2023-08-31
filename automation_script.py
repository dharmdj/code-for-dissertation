import subprocess

def check_image_vulnerabilities(image_name, image_tag):
    try:
        # Add the image for scanning
        add_image_cmd = f"anchore-cli image --username admin --password foobar --url http://localhost:8228/v1 add {image_name}:{image_tag}"
        subprocess.run(add_image_cmd, shell=True, check=True)

        # Wait for analysis to complete
        wait_image_cmd = f"anchore-cli image --username admin --password foobar --url http://localhost:8228/v1 wait {image_name}:{image_tag}"
        subprocess.run(wait_image_cmd, shell=True, check=True)

        # Get vulnerability information
        content_cmd = f"anchore-cli image content --username admin --password foobar --url http://localhost:8228/v1 {image_name}:{image_tag}"
        content_output = subprocess.check_output(content_cmd, shell=True, universal_newlines=True)

        # Print vulnerability information
        print(content_output)

    except subprocess.CalledProcessError as e:
        print("Error:", e)
        print("Vulnerability check failed.")

if __name__ == "__main__":
    image_name = "docker.io/library/openjdk"
    image_tag = "latest"

    check_image_vulnerabilities(image_name, image_tag)