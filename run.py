from market import app, db

# Push the app context
app.app_context().push()

# Create the database tables
with app.app_context():
    db.create_all()

    # Import Item model after creating the app context
    from market.models import Item

if __name__=='__main__':
    app.run(debug=True)