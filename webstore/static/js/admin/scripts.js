function sidebarActive(navLinkId_1, navLinkId_2 = ''){
    let navLink_1 = document.getElementById(navLinkId_1);
    if(navLinkId_1 != null){
        navLink_1.classList.add('active');

        let parentNode = navLink_1.parentNode
        if(parentNode.classList.contains('nav-item')){
            parentNode.classList.add('menu-open');
        }
    }


    if(navLinkId_2 != ''){
        let navLink_2 = document.getElementById(navLinkId_2);
        if(navLinkId_2 != null){
            navLink_2.classList.add('active');
        }
    }

}