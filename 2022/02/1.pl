#!/usr/bin/perl

my $sum=0;


while(<>)
{
    /(\w)\s(\w)/;
    if ($1 eq "A")
    {
	if ($2 eq "X") {$sum+=4;}
	elsif ($2 eq "Y") {$sum+=8;}
	elsif ($2 eq "Z") {$sum+=3;}
    }
    elsif ($1 eq "B")
    {
	if ($2 eq "X") {$sum+=1;}
	elsif ($2 eq "Y") {$sum+=5;}
	elsif ($2 eq "Z") {$sum+=9;}
    }
    elsif ($1 eq "C")
    {
	if ($2 eq "X") {$sum+=7;}
	elsif ($2 eq "Y") {$sum+=2;}
	elsif ($2 eq "Z") {$sum+=6;}
    }

    
}

print "$sum\n";
