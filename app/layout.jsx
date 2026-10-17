import "./globals.css";
export const metadata = {
  title: "Gravity Witness | PhysicsResearch",
  description: "An auditable scientific inquiry into an experiment that could distinguish quantum gravity from classical alternatives.",
  robots: { index: true, follow: true },
};
export default function RootLayout({ children }) {
  return <html lang="en"><body>{children}</body></html>;
}
