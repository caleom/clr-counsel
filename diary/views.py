from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry
from .forms import DiaryEntryForm

# Create your views here.
def diary_entries(request):
    diary_entries = DiaryEntry.objects.all()
    return render(request, 'diary/diary_entries.html', {'diary_entries': diary_entries})

@login_required
def create_diary_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            diary_entry = form.save(commit=False)
            diary_entry.user = request.user
            diary_entry.save()
            return redirect('home')  # Redirect to home page after successfully creating a diary entry
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/entry_form.html', {'form': form})