import datetime

class Blog:
    def __init__(self):
        self.posts = []
        # Liste codée en dur d’administrateurs
        self.admins = ['admin1@example.com', 'admin2@example.com']
        # Liste codée en dur d’abonnés
        self.subscribers = ['reader1@example.com', 'reader2@example.com']

    def new_post(self, title: str, content: str):
        """
        Crée un nouvel article, l'enregistre et déclenche :
         1. le log
         2. la notification des admins
         3. la notification des abonnés
        """
        post = {
            'title': title,
            'content': content,
            'created_at': datetime.datetime.now()
        }
        self.posts.append(post)

        # 1) Log inline — couplage direct
        self._log_post(post)

        # 2) Notification admins inline — couplage direct
        self._send_email_to_admins(post['title'])

        # 3) Notification abonnés inline — couplage direct
        self._notify_subscribers(post['title'])

    def _log_post(self, post: dict):
        """
        Journalisation basique : affiche date et titre.
        """
        timestamp = post['created_at'].strftime('%Y-%m-%d %H:%M:%S')
        print(f"[LOG] {timestamp} — Article créé : « {post['title']} »")

    def _send_email_to_admins(self, post_title: str):
        """
        Envoi d'e-mails aux administrateurs.
        """
        for admin in self.admins:
            print(f"[E-MAIL ADMIN] À : {admin} — L’article « {post_title} » est publié.")

    def _notify_subscribers(self, post_title: str):
        """
        Envoi d'e-mails aux abonnés.
        """
        for subscriber in self.subscribers:
            print(f"[E-MAIL ABONNÉ] À : {subscriber} — Nouvel article : « {post_title} » disponible !")

def main():
    blog = Blog()
    # Simulation de publications
    blog.new_post("Introduction à Python", "Bienvenue dans ce nouveau tutoriel sur Python.")
    blog.new_post("Les bases de l'OOP", "Aujourd'hui, on explore l'encapsulation, l'héritage et le polymorphisme.")

if __name__ == "__main__":
    main()