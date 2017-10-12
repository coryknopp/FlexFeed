class Member(models.Model):
    """
    Model representing a member.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sm_links = 
    stock = models.ManyToManyField('Stock', help_text="Select a stock for this member")
    post = models.ManyToManyField('Post', help_text="Select a post for this member")


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)
    
    
    def get_social_media_link(self):
        """
        Returns the link to a particular social media.
        """
        return reverse('author-detail', args=[str(self.id)])
    

