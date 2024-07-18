# Use the official Windows image
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Install necessary tools and dependencies
RUN powershell -Command \
    Install-WindowsFeature Web-Server; \
    Invoke-WebRequest -Uri https://aka.ms/vs/16/release/vs_buildtools.exe -OutFile vs_buildtools.exe; \
    Start-Process -Wait -NoNewWindow -FilePath .\vs_buildtools.exe -ArgumentList '--quiet --wait --norestart --nocache --installPath C:\BuildTools', '--add Microsoft.VisualStudio.Workload.VCTools', '--includeRecommended'

# Set environment variables
ENV PATH="C:\\BuildTools\\VC\\Tools\\MSVC\\14.28.29910\\bin\\Hostx64\\x64;${PATH}"
