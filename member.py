class Member(models.Model):
    """
    Model representing a member.
    """
    name = models.CharField(max_length=100)
    sm_links = models.URLField() 
    stock = models.OnetoOneField('Stock', help_text="Select a stock for this member")
    post = models.ForeignKey('Post', help_text="Select a post for this member")


    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s' % (self.name)
    

