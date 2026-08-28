## Part 1: Windows Setup (via Multipass)

### Step 1 — Install Multipass

1. Download the Multipass installer from: https://canonical.com/multipass/install
2. Run the installer — administrator privileges are required
3. Multipass uses **Hyper-V** by default on Windows 10/11 Pro or Enterprise. If you have Windows 10 Home, install VirtualBox first and Multipass will use that instead.
4. Open a Command Prompt or PowerShell and verify:

```powershell
multipass version
```

### Step 2 — Create the Ubuntu 24.04 VM

```powershell
multipass launch 24.04 --name <your-firstname-vm> --cpus 4 --memory 8G --disk 60G
```

This downloads and launches Ubuntu 24.04 LTS. It may take a few minutes on first run.

### Step 3 — Open a shell into the VM

```powershell
multipass shell <your-firstname-vm>
```

You are now inside the Ubuntu 24.04 VM.

### Useful Multipass Commands (Windows)

```powershell
multipass list              # list all VMs
multipass stop <your-firstname-vm>         # stop the VM
multipass start <your-firstname-vm>        # start the VM
multipass shell <your-firstname-vm>        # open a shell
multipass delete <your-firstname-vm>       # delete the VM
multipass purge             # permanently remove deleted VMs
```

---

## Part 2: Mac Setup (via Multipass)

### Step 1 — Install Multipass

**Option A — Download installer (recommended):**

1. Download from: https://canonical.com/multipass/install
2. Run the `.pkg` installer
3. Administrator privileges are required

**Option B — Homebrew:**

```bash
brew install --cask multipass
```

Verify installation:

```bash
multipass version
```

### Step 2 — Create the Ubuntu 24.04 VM

```bash
multipass launch 24.04 --name <your-firstname-vm> --cpus 4 --memory 8G --disk 60G
```

> **Note for Apple Silicon (M1/M2/M3/M4/M5):** Multipass uses QEMU with Apple's Hypervisor framework on ARM Macs. The VM will be ARM64 Ubuntu.

### Step 3 — Open a shell into the VM

```bash
multipass shell <your-firstname-vm>
```
You are now inside the Ubuntu 24.04 VM.

### Useful Multipass Commands (Mac)

```bash
multipass list              # list all VMs
multipass stop <your-firstname-vm>         # stop the VM
multipass start <your-firstname-vm>        # start the VM
multipass shell <your-firstname-vm>        # open a shell
multipass info <your-firstname-vm>         # show VM details including IP
multipass delete <your-firstname-vm>       # mark VM for deletion
multipass purge             # permanently remove deleted VMs
```
---

# Install Docker in a Multipass Ubuntu VM

## 1. Launch or access your Multipass VM
```bash
multipass launch --name <your-firstname-vm> --cpus 2 --memory 4G --disk 20G
```

## 2. Mount a shared folder from the host

This lets you edit code on the host (e.g. with VS Code) while running/testing it inside the VM.

```bash
multipass mount /path/on/host <your-firstname-vm>:/path/in/vm
```

Example:
```bash
multipass mount ~/projects/myapp <your-firstname-vm>:/home/ubuntu/myapp
```

Notes:
- Run this from the **host**, not inside the VM shell.
- The folder shows up inside the VM at the path you specify, and changes sync both ways.
- To stop sharing: `multipass umount <your-firstname-vm>:/path/in/vm`
- To list current mounts: `multipass info <your-firstname-vm>`


## 3. Update package index

```bash
multipass shell <your-firstname-vm>
sudo apt-get update
sudo apt-get upgrade -y
```

## 4. Install prerequisites
```bash
sudo apt-get install -y ca-certificates curl gnupg
```

## 5. Add Docker's official GPG key
```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
```

## 6. Add the Docker repository
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

## 7. Install Docker Engine
```bash
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

## 8. Verify installation
```bash
sudo docker run hello-world
```

## 9. (Optional) Run Docker without `sudo`
```bash
sudo usermod -aG docker $USER
```
Then exit and re-enter the shell (`exit`, then `multipass shell <your-firstname-vm>` again) for the group change to take effect.