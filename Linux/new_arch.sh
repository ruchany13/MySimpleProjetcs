//This script can use install a new Arch linux. you must be root.
pacman -Syyu
pacman -S xorg xorg-server xfce4 xfce4-goodies lightdm lightdm-gtk-greeter
echo "Xfce4 is ready"
systemctl enable lightdm.service
systemctl enable NetworkManager.service
pacman -S neofetch
pacman -S gedit
neofetch
