import Link from "next/link";
import Image from "next/image";

import logoImg from "@/assets/logo.png";
import classes from "./main-header.module.css";
import MainHeaderBackground from "./main-header-background";

export default function MainHeader() {
	return (
		<>
			<MainHeaderBackground />
			<header className={classes.header}>
				<Link href="/" className={classes.logo}>
					<Image src={logoImg} alt="NextLevel Food" priority />
					NextLevel Food
				</Link>

				<nav className={classes.nav}>
					<ul>
						<Link href="/meals">Browse Meals</Link>
						<Link href="/community">Foodies Community</Link>
					</ul>
				</nav>
			</header>
		</>
	);
}
